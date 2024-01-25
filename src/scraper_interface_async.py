import asyncio
import json
from concurrent.futures import ThreadPoolExecutor
from typing import List

import aiofiles
import aiohttp

from selenium import webdriver

from .core.schemas.data import Article


class WebScraperInterfaceAsync:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.executor = ThreadPoolExecutor(max_workers=1)

    async def fetch_html_selenium(self, session, url: str) -> str:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(self.executor, self.driver.get, url)
        return self.driver.page_source

    async def fetch_html(self, session: aiohttp.ClientSession, url: str) -> str:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
        except Exception as e:
            print(f"An error occurred while fetching HTML: {e}")
            return ""

    async def write_data(self, articles: List[Article], filename: str) -> None:
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)
        async with aiofiles.open(filename, "w", encoding="utf-8") as file:
            await file.write(formatted_json)

    async def extract_data(self, html: str) -> List[Article]:
        ...

    async def scrape(self, url: str, filename: str) -> None:
        async with aiohttp.ClientSession() as session:
            html = await self.fetch_html(session, url)
            articles = await self.extract_data(html)
            await self.write_data(articles, filename)

    async def scrape_selenium(self, url: str, filename: str) -> None:
        async with aiohttp.ClientSession() as session:
            html = await self.fetch_html_selenium(session, url)
            articles = await self.extract_data(html)
            await self.write_data(articles, filename)

    def close(self):
        self.driver.quit()
