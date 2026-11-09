import json
import os
import requests


def get_pokemon_data(character_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{character_name}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()

    types = []
    for pokemon_type in data["types"]:
        type_name = pokemon_type["type"]["name"]
        types.append(type_name)

    return {
        "name": data["name"].capitalize(),
        "height_m": data["height"] / 10,
        "weight_kg": data["weight"] / 10,
        "types": types,
        "image_url": data["sprites"]["front_default"]
    }


def save_profile(profile):
    filename = f'{profile["name"]}_profile.json'

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=2)

    return filename


def main():
    print("Welcome to the Pokédex!")
    character_name = input("Which Pokémon are you looking for? ").lower()
    print("\n... Searching the global database ...\n")
    profile = get_pokemon_data(character_name)
    if profile:
        filename = save_profile(profile)
        print(f"Success! Data for {profile['name']} was found.")
        print(f"The profile has been saved as '{os.path.abspath(filename)}'!")
    else:
        print("Pokémon not found.")


if __name__ == "__main__":
    main()