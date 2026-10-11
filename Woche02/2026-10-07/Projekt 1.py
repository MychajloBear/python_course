print("=" * 42+"\nGuten Tag! Ich bin der beste Taschenrechner!\nIch kann +, -, *, /, //, % und ** berechnen!\n"+"=" * 42)

while True:
    try:
        num1 = float(input("Tippe die erste Zahl ein... "))
        operator = input("Was willst du mit dieser Zahl tun? (+, -, *, /, //, %, **): ").strip()
        num2 = float(input("Tippe die zweite Zahl ein... "))
    except ValueError:
        print("Ungültige Eingabe! Bitte nur Zahlen.\n")
        continue

    print("=" * 42)
    
    error = False
    result = None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Fehler: Division durch Null.")
            error = True
        else:
            result = num1 / num2
    elif operator == "//":
        if num2 == 0:
            print("Fehler: Ganzzahldivision durch Null.")
            error = True
        else:
            result = num1 // num2
    elif operator == "%":
        if num2 == 0:
            print("Fehler: Modulo durch Null.")
            error = True
        else:
            result = num1 % num2
    elif operator == "**":
        result = num1 ** num2
    else:
        print("Unbekanntes Rechenzeichen!")
        error = True

    if not error:
        print(f"Das Ergebnis der Rechnung {num1} {operator} {num2} lautet {result} !\n"+"=" * 42)


    play_again = input("Noch einmal? (j/n): ").strip().lower()
    if play_again in ("n", "nein"):
        print("Auf Wiedersehen!")
        break
    print()