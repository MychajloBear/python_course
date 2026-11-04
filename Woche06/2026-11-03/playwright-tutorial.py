
import playwright
from playwright.sync_api import sync_playwright
import time

url = "https://de.wikipedia.org"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    time.sleep(3)
    page.goto(url)
    time.sleep(3)

    page.locator("#searchInput").fill("Python (Programmiersprache)")
    time.sleep(3)
    page.keyboard.press("Enter")
    page.locator("h1").wait_for()
    titel = page.locator("h1").inner_text()
    print(titel)