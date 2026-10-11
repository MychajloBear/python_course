import random

print("="*42)
print("WÜRFELSIMULATOR 3000")
print("="*42)

while True:
  try:
    d_sides = int(input("Wie viele Seiten soll der Würfel haben? (z.B. 6): "))
    num_rolls = int(input("Wie viele Würfe sollen simuliert werden? "))

    if d_sides < 1 or num_rolls < 1:
      print("Bitte gib Zahlen größer als 0 ein.")
      continue
  except ValueError:
    print("Ungültige Eingabe! Bitte gib ganze Zahlen ein.")
    continue

  print("="*42)
  print(f"Simuliere {num_rolls} Würfe mit einem {d_sides}-seitigen Würfel...")
  print("="*42)

  results = []
  for _ in range(num_rolls):
    roll = random.randint(1, d_sides)
    results.append(roll)

  empirical_mean = sum(results) / num_rolls
  theoretical_mean = (d_sides + 1) / 2

  print(f"Berechneter Mittelwert: {empirical_mean:.3f}")
  print(f"Theoretischer Mittelwert: {theoretical_mean}")
  print("="*42)

  play_again = input("Noch einmal? (j/n): ").strip().lower()
  if play_again != "j":
    print("Programm beendet. Bis zum nächsten Mal!")
    break