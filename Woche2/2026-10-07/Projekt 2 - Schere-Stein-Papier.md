# ✂️ 🪨 📄 Projekt: Schere, Stein, Papier

In diesem Projekt programmierst du das interaktive Spiel **Schere, Stein, Papier**.

Wir bauen das Spiel Schritt für Schritt auf. Zuerst entwickelst du die Logik mit festen Werten, und im Anschluss machst du das Spiel durch echte Eingaben und eine Schleife richtig dynamisch!

### 📜 Die Spielregeln
* ✂️ **Schere** schneidet 📄 **Papier** *(Schere gewinnt)*
* 📄 **Papier** umhüllt 🪨 **Stein** *(Papier gewinnt)*
* 🪨 **Stein** schlägt ✂️ **Schere** *(Stein gewinnt)*
* 🤝 Wählen beide das Gleiche, ist es ein **Unentschieden**.


### 🛠️ Deine Aufgaben

**Schritt 1: Basis-Setup & Schiedsrichter-Logik**
* Erstelle zwei Variablen: `spieler_1` und `spieler_2` und weise ihnen zum Testen erst einmal feste Texte zu (z. B. `"Schere"` und `"Stein"`).
* Schreibe eine `if`-`elif`-`else`-Struktur, die die Werte der beiden Variablen miteinander vergleicht.
* Gib am Ende per `print()` aus, wie die Runde ausgegangen ist.
> 💡 **Tipp zum Testen:** Ändere die festen Werte manuell ein paar Mal, um zu prüfen, ob alle Gewinn-Kombinationen und das Unentschieden richtig erkannt werden.

**Schritt 2: Echte Spieler-Eingaben (`input`)**
* Wenn deine Logik aus Schritt 1 fehlerfrei funktioniert, entfernen wir die "fest einprogrammierten" (hardgecodeten) Werte.
* Nutze nun die `input()`-Funktion, damit beide Spieler ihre Wahl in die Konsole eintippen können (z. B. `"Spieler 1, wähle Schere, Stein oder Papier: "`).

**Schritt 3: Das Spiel wiederholen (`while`-Schleife)**
* Niemand spielt gerne nur eine einzige Runde! Packe deine gesamte Spiel-Logik (Eingaben, Auswertung und Ausgabe) in eine `while`-Schleife.
* Frage die Spieler am Ende jedes Durchlaufs per `input()`, ob sie noch eine Runde spielen wollen (z. B. `"Wollt ihr weiterspielen? (ja/nein): "`).
* Erstelle eine Bedingung, die überprüft, was eingegeben wurde. Wenn die Antwort `"nein"` lautet, soll die Schleife (und damit das Spiel) beendet werden.


### 🌟 Bonusaufgabe: Mensch vs. Maschine
Hast du keinen zweiten Spieler parat? Dann lass den Computer den Part von Spieler 2 übernehmen!
* Importiere ganz oben in deinem Code das Modul für Zufallszahlen: `import random`
* Ersetze die `input()`-Abfrage von `spieler_2` durch die Wahl des Computers.
* Der Computer soll seine Wahl zufällig aus einer Liste treffen. Nutze dafür den Befehl: `random.choice(["Schere", "Stein", "Papier"])`
* Vergiss nicht, die Wahl des Computers per `print()` auszugeben, damit der menschliche Spieler weiß, wogegen er gerade gespielt hat!