class Fahrzeug:
    def __init__(self, marke: str, modell: str, baujahr: int):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def anzeigen(self):
        print(f"Marke: {self.marke} | Modell: {self.modell} | Baujahr: {self.baujahr}")

    def starten(self):
        print(f"Das Fahrzeug ({self.marke} {self.modell}) wird gestartet.")

    def hupe(self):
        print(f"{self.marke} {self.modell} hupt: Beep! Beep!")