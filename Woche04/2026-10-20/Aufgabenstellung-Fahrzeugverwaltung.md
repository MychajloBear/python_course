# Projektaufgabe: Fahrzeugverwaltung mit OOP und Vererbung
## Ziel

Erstelle ein Python-Programme (``.py``-Datei) zur Verwaltung von Fahrzeugen. Dabei sollst du die Grundlagen der objektorientierten Programmierung (OOP) sowie Vererbung anwenden.
Jede Klasse und Unterklasse bekommt ihre eigene Python-Datei. Zusätzlich soll eine ``main.py`` erstellt werden, die die Unterklassen importiert und die Ausgaben auf der Konsole erstellt.

### 1. Erstellung der Basisklasse

Erstelle die Basisklasse Fahrzeug. Die Klasse soll folgende Attribute besitzen:
- ``marke``
- ``modell``
- ``baujahr``

Implementiere außerdem folgende Methoden:

- ``anzeigen()``: Gibt alle Informationen zum Fahrzeug aus.
- ``starten()``: Gibt eine allgemeine Meldung aus, dass das Fahrzeug gestartet wird.
- (Optional) Erfinde eine eigene Methode, die zu deinem Fahrzeug passt.

### 2. Erstellung von drei Unterklassen

Wähle eine oder mehrere der folgenden Klassen aus, die als Unterklasse implementiert wird:
- ``Auto``
- ``Motorrad``
- ``LKW``
- ...oder etwas ganz anderes? 

Jede Unterklasse soll als Python-Datei erstellt werden. Beispiele: ``auto.py``, ``motorrad.py``,``lkw.py`` usw.

#### Anforderungen
- Jede Unterklasse soll von Fahrzeug erben. Verwende ``super().__init__(...)``, um den Konstruktor der Basisklasse aufzurufen.
- Überschreibe die Methode ``starten()`` in jeder Unterklasse, sodass eine fahrzeugspezifische Ausgabe erscheint.
- (Optional) Erfinde eine eigene Methoden, die zu deinen Fahrzeugen passt.

### 3. Ausgaben auf der Konsole
- Erstelle eine ``main.py``, um dort die Anzeigelogiken zu implementieren.
- Erzeuge mindestens ein Objekt jeder Unterklasse.
- Gib die Fahrzeugdaten mit ``anzeigen()`` aus.
- Starte das Fahrzeug mit ``starten()``.
- Rufe anschließend deine zusätzlichen Methoden auf.
- (Optional) Versuche eine hübschere Konsolenausgabe zu erstellen