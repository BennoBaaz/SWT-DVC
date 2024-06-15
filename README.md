# SWT-DVC
Einsendeaufgabe DVC für den Kurs Softwaretechnik 

1. Erstellen Sie sich ein Repository in Github oder GitLab.

2. Pushen Sie ein eigenes Projekt von Ihnen hoch (z.B. das CCD-Projekt) oder erstellen Sie ein neues Projekt!
    So habe ich meine Datein in der Projekt geladen/gepushed.
![Push der Projektdatein](/Images/2-Push.png)

3. Wenden Sie alle in den Unterlagen genannten relevanten Methoden beweisbar an: (das Github Repo ist Beweis) push, pull, add, commit, diff, status, rm/mv, etc.
    Folgende Befehle habe ich verwendet. Dafür habe ich eine Testdatei angelegt und diese bearbeitet.
![Anwenden der Methoden Status, Add, Diff](/Images/3-status,add,diff.png)
![Anwenden der Methoden Push, Pull, mv und Commit](/Images/3-push,pull,mv,commit.png)

4. Experimentieren Sie mit Zeitreisen!

Ich habe mir über den Befehl "git log" alle Commits ausgeben lassen
![Historie aller Commits](/Images/4-Log.png)

Danach habe ich mir einen alten Commit geladen. Dadurch hat sich auch meine Dateistruktur im VS-Code-Explorer aktualisiert.
Explorer vor dem wechsel:
![Explorer des akteullen Commits](/Images/4-neu.png)

Befehl zum laden des alten Commits:
![Wechseln in alten Commit](/Images/4-pastCommit.png)

Explorer nach dem Wechsel:
![Explorer des alten Commits](/Images/4-alt.png)

5. Erstellen sie zwei unterschiedliche aber ähnliche Branches, wechseln sie hin und her und mergen sie diese Branches dann wieder!

Ich habe 2 Branches erstellt und in diesem die Testdatei.txt angepasst:
![Branches erstellt und Testdatei angepasst](/Images/5-branches_erstellen.png)

Dann wollte ich diese wieder mergen, aber weil die Testdatei in beiden Branches verändert wurde, gab es eine Fehlermeldung:
![Merge1 mit Fehlermeldung](/Images/5-branches-merge1.png)

Nach dem Beheben dieses Merge-Conflicts konnte ich die branches wieder mergen:
![Merge2 ohne Fehlermeldung](/Images/5-branches-merge2.png)

6. Erstellen Sie in GitHub einen Pull-Request bezugnehmend auf https://github.com/edlich/education! Bitte referenzieren Sie auf den Pull-Request mit Link oder der Pull-Request Nummer! Kryptische GitHub Namen kann ich kaum zuordnen. Die Aufgabenteile vor dem Pull-Request bitte nicht in den Pull-Request einbauen, sondern extra abgeben!
