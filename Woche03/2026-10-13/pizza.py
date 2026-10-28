menu = {}
def display_menu(menu_from_file):
    print("--- Speisekarte ---")
    for dish, price in menu_from_file.items():
        print(f"- {dish}: {price} €")
    print("-" * 20)

def load_menu(file_path):
    menu.clear()
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if ";" in line:
                dish, price = line.strip().split(";")
                menu[dish.strip().lower()] = float(price.strip())

def proceed_order():    
    order = input("\nWas möchten Sie bestellen? (oder 'ende' zum Beenden): ").strip().lower()
    if order == "ende":
        print("Vielen Dank die Bestellung! Bye!")
        return False
    if order in menu:
        price = menu[order]
        print(f"Sie haben '{order}' für {price} € bestellt.")
        with open("orders.txt", "a", encoding="utf-8") as order_file:
            order_file.write(f"Bestellung: {order} - {price} €\n")
        print("Die Bestellung gespeichert.")
    else:
        print(f"Sorry, '{order}' ist nicht auf der Menu.")
    return True
   
load_menu("menu.txt")
display_menu(menu)

while proceed_order():
    print("\nWillkommen!")
    