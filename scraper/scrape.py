import asyncio
from playwright.async_api import async_playwright
import json

OUTPUT_FILE = "data.json"

async def scrape():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Open NepseAlpha market page
        await page.goto("https://nepsealpha.com/trading/chart", timeout=60000)

        # Wait for JS to load
        await page.wait_for_timeout(5000)

        # Extract data from page
        data = await page.evaluate("""
        () => {
            const stocks = window.__NUXT__?.data?.[0]?.stockData || [];
            return stocks.map(s => ({
                symbol: s.symbol,
                lastTradedPrice: s.ltp
            }));
        }
        """)

        await browser.close()

        with open(OUTPUT_FILE, "w") as f:
            json.dump(data, f)

asyncio.run(scrape())