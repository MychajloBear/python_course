from auto import Auto
from motorrad import Motorrad
from lkw import LKW

def main():
    print("=" * 60)
    print("FAHRZEUGVERWALTUNGSSYSTEM (OOP & VERERBUNG)")
    print("=" * 60)

    mein_auto = Auto("Volkswagen", "Golf GTI", 2022, 5)
    mein_motorrad = Motorrad("Yamaha", "MT-07", 2023, 689)
    mein_lkw = LKW("Mercedes-Benz", "Actros", 2021, 18.5)

    fahrzeuge = [mein_auto, mein_motorrad, mein_lkw]

    for i, f in enumerate(fahrzeuge, 1):
        print(f"\n--- Fahrzeug {i} ---")
        f.anzeigen()
        f.starten()
        f.hupe()
        
        if isinstance(f, Auto):
            f.kofferraum_oeffnen()
        elif isinstance(f, Motorrad):
            f.wheelie_machen()
        elif isinstance(f, LKW):
            f.ladeflaeche_kippen()

    print("\n" + "=" * 60)
    print(" Alle Operationen erfolgreich ausgeführt.")
    print("=" * 60)

if __name__ == "__main__":
    main()