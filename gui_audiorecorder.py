import tkinter as tk
from tkinter import messagebox
import urllib.request
import datetime
import os
import threading

def record_audio(url, filename, duration, blocksize):
    stop_event = threading.Event()

    def update_countdown(count):
        if stop_event.is_set():
            return
        if count > 0:
            countdown_label.config(text=f"Recording... {count} seconds left")
            root.after(1000, update_countdown, count - 1)
        else:
            stop_event.set()
            messagebox.showinfo("Recording Complete", f"Recording saved as {filename}.mp3")
            countdown_popup.destroy()

    def cancel_recording():
        stop_event.set()
        countdown_popup.destroy()

    def recording():
        start_time = datetime.datetime.now()
        try:
            with urllib.request.urlopen(url) as stream:
                with open(filename + '.mp3', 'wb') as outfile:
                    while ((datetime.datetime.now() - start_time).seconds < duration):
                        if stop_event.is_set():
                            break
                        outfile.write(stream.read(blocksize))
        except Exception as e:
            messagebox.showerror("Recording Error", f"An error occurred during recording:\n{e}")

    countdown_popup = tk.Toplevel(root)
    countdown_popup.title("Recording")
    countdown_popup.geometry("300x150")

    countdown_label = tk.Label(countdown_popup, text=f"Recording... {duration} seconds left")
    countdown_label.pack(pady=20)

    cancel_button = tk.Button(countdown_popup, text="Cancel", command=cancel_recording)
    cancel_button.pack(pady=10)

    recording_thread = threading.Thread(target=recording)
    recording_thread.start()

    update_countdown(duration)

def list_recordings():
    recordings = [f for f in os.listdir() if f.endswith(".mp3")]
    if recordings:
        messagebox.showinfo("Recordings", "List of recordings:\n{}".format('\n'.join(recordings)))
    else:
        messagebox.showinfo("No Recordings", "No recordings found.")

def start_recording():
    url = url_entry.get() if url_entry.get() else "https://stream.skymedia.ee/live/NRJdnb"
    filename = filename_entry.get() if filename_entry.get() else datetime.datetime.now().isoformat(timespec='seconds').replace(':', '')
    duration = int(duration_entry.get()) if duration_entry.get() else 30
    blocksize = int(blocksize_entry.get()) if blocksize_entry.get() else 64
    record_audio(url, filename, duration, blocksize)

root = tk.Tk()
root.title("Audio Recorder")

def create_label_entry_hint(frame, label_text, hint_text, row):
    label = tk.Label(frame, text=label_text, width=20, anchor='w')
    label.grid(row=row, column=0, sticky="w", pady=2)

    entry = tk.Entry(frame, width=50)
    entry.grid(row=row, column=1, padx=5, pady=2)

    hint = tk.Label(frame, text=hint_text, anchor='w')
    hint.grid(row=row + 1, column=1, sticky="w", padx=5)
    
    return entry

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

url_entry = create_label_entry_hint(frame, "URL:", "Default: https://stream.skymedia.ee/live/NRJdnb", 0)
filename_entry = create_label_entry_hint(frame, "Filename:", "Default: " + datetime.datetime.now().isoformat(timespec='seconds').replace(':', ''), 2)
duration_entry = create_label_entry_hint(frame, "Duration (seconds):", "Default: 30", 4)
blocksize_entry = create_label_entry_hint(frame, "Blocksize (bytes):", "Default: 64", 6)

record_button = tk.Button(frame, text="Record", command=start_recording)
record_button.grid(row=8, column=0, columnspan=2, pady=10)

list_button = tk.Button(frame, text="List Recordings", command=list_recordings)
list_button.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
