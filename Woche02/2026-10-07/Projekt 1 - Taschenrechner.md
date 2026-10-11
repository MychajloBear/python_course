# 🧮 Projekt: Einfacher Taschenrechner

In diesem Projekt programmierst du deinen eigenen Taschenrechner! Er soll auf Benutzereingaben reagieren, verschiedene mathematische Operationen durchführen und so lange laufen, bis der Benutzer ihn beenden möchte.

### 🛠️ Deine Aufgaben

**Schritt 1: Die Dateneingabe**
* Bitte den Benutzer um die Eingabe der ersten Zahl. Wandle diese Eingabe in eine Kommazahl (`float`) um.
* Bitte den Benutzer um die Auswahl eines Rechenzeichens. Unterstützt werden sollen mindestens: `+`, `-`, `*`, `/`, `//` (Ganzzahldivision), `%` (Modulo) und `**` (Potenz).
* Bitte den Benutzer um die Eingabe der zweiten Kommazahl.

**Schritt 2: Die Rechenlogik**
* Nutze eine `if`-`elif`-`else`-Struktur, um zu prüfen, welches Rechenzeichen eingegeben wurde.
* Führe die entsprechende Rechnung mit den beiden Zahlen durch.
* Gib die komplette Rechnung und das Ergebnis übersichtlich in der Konsole aus.
* *Tipp:* Denke daran, eine Fehlermeldung einzubauen, falls der Benutzer versucht, durch 0 zu teilen (bei `/`, `//` oder `%`)!

**Schritt 3: Der Dauerbetrieb (`while`-Schleife)**
* Packe das gesamte Programm in eine `while`-Schleife, damit der Taschenrechner nach einer Rechnung nicht direkt ausgeht.
* Frage den Benutzer am Ende jeder Rechnung, ob er eine weitere Berechnung durchführen möchte (z. B. mit "ja" oder "nein").

---

### 💻 Beispiel für einen Programmablauf

Deine Konsolenausgabe könnte ungefähr so aussehen (du kannst die Texte natürlich nach Belieben kreativ anpassen):

```
===============================================
Guten Tag!
Ich bin der beste Taschenrechner!
Ich kann +, −, ×, /, //, % und ** berechnen!
===============================================
Tippe die erste Zahl ein...                  5
Was willst du mit dieser Zahl tun?           +
Tippe die zweite Zahl ein...                 7
===============================================
Das Ergebnis der Rechnung 5 + 7 lautet 12 !
===============================================
Noch einmal? (j/n)
```