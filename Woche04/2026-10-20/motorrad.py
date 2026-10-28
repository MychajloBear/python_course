from fahrzeug import Fahrzeug

class Motorrad(Fahrzeug):
    def __init__(self, marke: str, modell: str, baujahr: int, hubraum: int):
        super().__init__(marke, modell, baujahr)
        self.hubraum = hubraum

    def anzeigen(self):
        super().anzeigen()
        print(f"-> Typ: Motorrad | Hubraum: {self.hubraum} ccm")

    def starten(self):
        print(f"Das Motorrad {self.marke} {self.modell} brüllt mit {self.hubraum}ccm Hubraum auf!")

    def wheelie_machen(self):
        print(f"{self.marke} {self.modell} zieht einen spektakulären Wheelie!")