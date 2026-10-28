from fahrzeug import Fahrzeug

class LKW(Fahrzeug):
    def __init__(self, marke: str, modell: str, baujahr: int, nutzlast_tonnen: float):
        super().__init__(marke, modell, baujahr)
        self.nutzlast_tonnen = nutzlast_tonnen

    def anzeigen(self):
        super().anzeigen()
        print(f"-> Typ: LKW | Nutzlast: {self.nutzlast_tonnen} Tonnen")

    def starten(self):
        print(f"Der LKW {self.marke} {self.modell} startet den schweren Dieselmotor mit Druckluft.")

    def ladeflaeche_kippen(self):
        print(f"Die Ladefläche des {self.marke} {self.modell} (Nutzlast: {self.nutzlast_tonnen}t) wird gekippt.")