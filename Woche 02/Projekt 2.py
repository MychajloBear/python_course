import random

print("-" * 42+"\nWillkommen!\n"+"-" * 42)

while True:
    player_choice = input("Wähle aus: Schere, Stein, Papier: ").strip().capitalize()
    
    values_list = ["Schere", "Stein", "Papier"]
    computer_choice = random.choice(values_list)
    
    if player_choice not in values_list:
        print("Ungültige Eingabe!\n")
        continue
        
    print(f"Du hast gewählt: {player_choice}")
    print(f"Der Computer: {computer_choice}")
    
    if player_choice == computer_choice:
        print("Unentschieden!\n")
    elif (player_choice == "Schere" and computer_choice == "Papier") or \
         (player_choice == "Papier" and computer_choice == "Stein") or \
         (player_choice == "Stein" and computer_choice == "Schere"):
        print("Du hast gewonnen!\n")
    else:
        print("Schade,KI hat gewonnen!\n")

    play_again = input("Noch eine Runde spielen? (ja/nein): ").strip().lower()
    if play_again.capitalize().strip in ("n","nein"):
        print("Danke! Chao.")
        break
