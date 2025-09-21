import requests
from bs4 import BeautifulSoup
import uuid
import os
from playwright.async_api import async_playwright

def fetch_metadata(url: str) -> dict:
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")

    title = soup.title.string if soup.title else None
    desc = soup.find("meta", attrs={"name": "description"})
    og_image = soup.find("meta", property="og:image")

    return {
        "title": title,
        "description": desc["content"] if desc else None,
        "og_image": og_image["content"] if og_image else None,
        "url": url
    }

async def take_screenshot(url: str) -> str:
    filename = f"{uuid.uuid4()}.png"
    folder = "app/screenshots"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, timeout=15000)
        await page.screenshot(path=path)
        await browser.close()

    return path
