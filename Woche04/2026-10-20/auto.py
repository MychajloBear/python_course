from fahrzeug import Fahrzeug
import random

class Auto(Fahrzeug):
    def __init__(self, marke: str, modell: str, baujahr: int, tueren: int):
        super().__init__(marke, modell, baujahr)
        self.tueren = tueren

    def anzeigen(self):
        super().anzeigen()
        print(f"-> Typ: Auto | Türen: {self.tueren}")

    def starten(self):
        print(f"Das Auto {self.marke} {self.modell} startet den Verbrennungsmotor leise und geschmeidig.")

    def kofferraum_oeffnen(self):
        print(f"Der Kofferraum des {self.marke} {self.modell} ({self.tueren}-Türer) wird geöffnet.")