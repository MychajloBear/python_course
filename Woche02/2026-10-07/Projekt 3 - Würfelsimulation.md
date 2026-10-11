# 🎲 Projekt: Würfelsimulator 3000

In diesem Projekt übernimmst du die Aufgabe, das Werfen eines fairen Würfels zu simulieren. Ziel ist es, die geworfenen Augenzahlen zu sammeln und daraus den Durchschnitt (Mittelwert) zu berechnen. So kannst du überprüfen, ob sich das Ergebnis bei vielen Würfen dem theoretischen Erwartungswert annähert!

### 🛠️ Deine Aufgaben

**Schritt 1: Die Simulation**
* Frage den Benutzer per `input`, wie viele Würfe simuliert werden sollen.
* Verwende eine Schleife, um den Würfel entsprechend oft zu werfen.
* Nutze die Funktion `randint` aus dem `random`-Modul, um für jeden Wurf eine zufällige Zahl zwischen 1 und 6 zu generieren.
* Speichere die Ergebnisse aller Würfe in einer Liste.

**Schritt 2: Auswertung & Vergleich**
* Berechne den empirischen (tatsächlichen) Mittelwert: Addiere dafür alle Zahlen in deiner Liste und teile das Ergebnis durch die Anzahl der Würfe.
* Gib deinen berechneten Mittelwert und den theoretischen Erwartungswert (dieser liegt bei einem normalen 6-seitigen Würfel bei 3,5) in der Konsole aus.
* *Experiment:* Beobachte, wie sich dein berechneter Wert verändert, wenn du z. B. nur 10, dann 100 und schließlich 10.000 Würfe simulierst!

**Schritt 3: Der Dauerbetrieb**
* Packe das Programm in eine `while`-Schleife, damit der Benutzer nach einem Durchgang direkt eine neue Simulation starten kann.

---

### 🌟 Bonusaufgabe: Eigene Würfel
Nicht jeder Würfel hat 6 Seiten (in Rollenspielen gibt es z.B. auch 4- oder 20-seitige Würfel).
* Passe dein Programm so an, dass der Benutzer am Anfang gefragt wird, wie viele Seiten der Würfel haben soll.
* *Tipp:* Der theoretische Erwartungswert ändert sich dann! Er berechnet sich durch `(Seitenanzahl + 1) / 2`.

---

### 💻 Beispiel für einen Programmablauf

Deine Konsolenausgabe könnte so aussehen:

```
===============================================
WÜRFELSIMULATOR 3000
===============================================
Wie viele Würfe sollen simuliert werden?
10000
===============================================
Simuliere 10000 Würfe...
===============================================
Berechneter Mittelwert: 3.511
Theoretischer Mittelwert: 3.5
===============================================
Noch einmal? (j/n)
```