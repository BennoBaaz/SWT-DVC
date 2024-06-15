import urllib.request
import datetime
import argparse
import os

def record_audio(url, filename, duration, blocksize):
    """Funktion zur Aufnahme der gegebenen URL abhaengig von der angegebenen "duration" und "blocksize". Speichert Datei mit dem "filename" ab.
    

    Args:
        url (string): stream url
        filename (string): name of mp3 file
        duration (int): duration of recording
        blocksize (int): blocksize of recording
    """
    # Öffnen der URL 
    with urllib.request.urlopen(url) as stream:
        # Festlegen der Zieldatei mit Schreibzugriff(binär)
        with open(filename + '.mp3', 'wb') as outfile:
            # Schleife zum Lesen von Daten
            while ((datetime.datetime.now() - start_time).seconds < duration):
                # Schreiben der Informationen in die Zeildatei
                outfile.write(stream.read(blocksize))
    
def list_recordings():
    """Funktion zur Auflistung aller Aufnahmen im Verzeichnis.
    """
    # Liste aller Dateien im aktuellen Verzeichnis, die mit '.mp3' enden
    recordings = [f for f in os.listdir() if f.endswith(".mp3")]
    # Überprüfung, ob Aufnahmen gefunden wurden
    if recordings:
        print("Liste der bisherigen Aufnahmen:")
        # Durchlaufe alle gefundenen Aufnahmen und gebe ihre Namen aus
        for recording in recordings:
            print(recording)
    else:
        # Fehlermeldung, falls keine Aufnahmen vorhanden sind
        print("Es wurde bisher nichts aufgenommen.")
    

start_time = datetime.datetime.now()

# Argumentenparser fuer die Kommandozeilenargumente
parser = argparse.ArgumentParser(description="CLI Audiorecorder")

# Definieren der erforderlichen Argumente
parser.add_argument("--url", help="stream-url", default="https://stream.skymedia.ee/live/NRJdnb")
parser.add_argument("--filename", help="filename", default=datetime.datetime.now().isoformat(timespec='seconds').replace(':', ''))
parser.add_argument("--duration", type=int, help="duration of the recording", default=30)
parser.add_argument("--blocksize", type=int, help="blocksize in bytes", default=64)
parser.add_argument("--list", action="store_true", help="list of recordings")

# Parsen der uebergebenen Argumente
args = parser.parse_args()

# ueberpruefen, ob die Option --list angegeben wurde
if args.list:
    # Wenn --list angegeben ist, rufe die Funktion list_recordings() auf
    list_recordings()
else:
    # Sonst rufe die Funktion record_audio() auf
    record_audio(args.url, args.filename, args.duration, args.blocksize)

