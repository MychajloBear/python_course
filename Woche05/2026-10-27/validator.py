import logging

logging.basicConfwig(
    filename="eingabevalidierung.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ValidationError(Exception):
    pass


def check_email(email):
    if "@" not in email:
        raise ValidationError("Die E-Mail-Adresse muss ein @ enthalten.")
    if "." not in email:
        raise ValidationError("Die E-Mail-Adresse muss einen Punkt (.) enthalten.")
    return True


def check_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Das Alter muss eine Zahl sein.")

    if age < 18 or age > 99:
        raise ValidationError("Alter muss zwischen 18 und 99 liegen.")

    return True


def check_password(password):
    if len(password) < 6:
        raise ValidationError(
            "Das Passwort muss mindestens 6 Zeichen lang sein."
        )

    if not any(char.isupper() for char in password):
        raise ValidationError(
            "Das Passwort muss mindestens einen Großbuchstaben enthalten."
        )

    if not any(char.isdigit() for char in password):
        raise ValidationError(
            "Das Passwort muss mindestens eine Zahl enthalten."
        )

    return True


def email_eingabe():
    while True:
        try:
            email = input("E-Mail-Adresse: ")
            check_email(email)

            print("\nDie eingegebene E-Mail ist gültig.")
            logging.info(f"Valid email entered: {email}")
            return

        except ValidationError as e:
            print(f"Fehler: {e}")
            logging.warning(f"Invalid email entered: {email} - {e}")


def alter_eingabe():
    while True:
        try:
            alter = input("Alter: ")
            check_age(alter)

            print("\nDas eingegebene Alter ist gültig.")
            logging.info(f"Valid age entered: {alter}")
            return

        except ValueError as e:
            print(f"Technischer Fehler: {e}")
            logging.warning(f"Invalid age entered: {alter} - {e}")

        except ValidationError as e:
            print(f"Fehler: {e}")
            logging.warning(f"Invalid age entered: {alter} - {e}")


def passwort_eingabe():
    while True:
        try:
            password = input("Passwort: ")
            check_password(password)

            print("\nDas eingegebene Passwort ist gültig.")
            logging.info("Valid password entered.")
            return

        except ValidationError as e:
            print(f"Fehler: {e}")
            logging.warning(f"Wrong Password - {e}")


def main():
    logging.info("Program is started")

    print("Willkommen zur Eingabevalidierung!")
    print("\nDrücke:")
    print("w -> Weiter")
    print("b -> Beenden")

    while True:
        auswahl = input("Bitte gib w oder b ein: ").lower()

        if auswahl == "b":
            print("Programm beendet.")
            logging.info("Program is closed.")
            return

        if auswahl == "w":
            break

        print("Ungültige Eingabe. Bitte w oder b eingeben.")

    email_eingabe()
    alter_eingabe()

    print("\nAlle bisherigen Eingaben sind gültig.")

    while True:
        antwort = input("\nMöchtest du ein Passwort prüfen? (j/n): ").lower()

        if antwort == "j":
            passwort_eingabe()
            break

        elif antwort == "n":
            break

        else:
            print("Bitte j oder n eingeben.")

    print("\nVielen Dank!")
    logging.info("Successful completion.")


if __name__ == "__main__":
    main()