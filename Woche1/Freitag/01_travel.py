destination = input("Destination: ")
days = int(input("Number of travel days: "))
travelers_amount = int(input("Number of travelers: "))
flight_cost = float(input("Flight (€): "))
hotel_cost = float(input("Hotel (€): "))
rental_car_cost = float(input("Rental car (€): "))

total_cost = flight_cost + hotel_cost + rental_car_cost
cost_per_person = total_cost / travelers_amount
cost_per_day = total_cost / days
day_type = "even" if days % 2 == 0 else "odd"

costs = [flight_cost, hotel_cost, rental_car_cost]
trip_info = (destination, days, travelers_amount)

trip_summary = {
    "Destination": destination,
    "Total cost": total_cost,
    "Cost per Person": cost_per_person,
    "Cost per Day": cost_per_day
}

print("\n--- Travel Cost Summary ---")
print(f"Destination: {destination} ({days} days)")
print("---------------------------")
print(f"Total cost: {total_cost:.2f} €")
print(f"Cost per person: {cost_per_person:.2f} €")
print(f"Cost per day for all: {cost_per_day:.2f} €")
print(f"[The number of days is {day_type}]")