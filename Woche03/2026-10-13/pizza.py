menu = {}

with open("menu.txt", "r", encoding="utf-8") as file:
    for line in file:
        if ";" in line:
            dish, price = line.strip().split(";")
            menu[dish.strip().lower()] = float(price.strip())

print("--- Speisekarte ---")
for dish, price in menu.items():
    print(f"- {dish}: {price} €")
print("-" * 20)

while True:
    order = input("\nWas möchten Sie bestellen? (oder 'ende' zum Beenden): ").strip().lower()

    if order == "ende":
        print("Vielen Dank die Bestellung! Bye!")
        break

    if order in menu:
        price = menu[order]
        print(f"Sie haben '{order}' für {price} € bestellt.")

        with open("orders.txt", "a", encoding="utf-8") as order_file:
            order_file.write(f"Bestellung: {order} - {price} €\n")
        
        print("Die Bestellung gespeichert.")
    else:
        print(f"Sorry, '{order}' ist nicht auf der Menu.")