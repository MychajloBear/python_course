import json
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright


URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
HISTORY_FILE = Path("price_history.json")


def scrape_book_data():
    with sync_playwright() as p:
        print("Starting browser...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print("Visiting website...")
        page.goto(URL)
        title = page.locator("h1").text_content()
        price_text = page.locator(".price_color").text_content()
        browser.close()
    price = float(price_text.replace("£", ""))
    return title, price


def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def main():
    title, price = scrape_book_data()

    print(f"Title found: {title}")
    print(f"Price found: £{price:.2f}")

    history = load_history()

    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "price": price
    }

    history.append(new_entry)

    save_history(history)

    print("The price has been logged successfully!")
    print(f"History file: {HISTORY_FILE.resolve()}")


if __name__ == "__main__":
    main()