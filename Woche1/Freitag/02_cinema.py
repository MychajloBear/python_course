CHILD_PRICE = 5.0
ADULT_PRICE = 10.0

print("---------- Welcome to the Cinema Ticket Programm ----------")
print(f"Prices: Children {CHILD_PRICE}€ | Adults {ADULT_PRICE}€")
print("------------------------------------------------------------")

child_tickets = int(input("How many child tickets do you like to have? "))
adult_tickets = int(input("How many adult tickets do you want to buy? "))

child_cost = child_tickets * CHILD_PRICE
adult_cost = adult_tickets * ADULT_PRICE
total_cost = child_cost + adult_cost

print("\n------------------------------------------------------------")
print(f"Cost for children: {child_cost:.2f}€")
print(f"Cost for adults: {adult_cost:.2f}€")
print(f"Total ticket price: {total_cost:.2f}€")
print("Thank you for your order and enjoy the movie!")
print("------------------------------------------------------------")