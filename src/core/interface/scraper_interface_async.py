import asyncio
import json
import logging
from concurrent.futures import ThreadPoolExecutor

import aiofiles
import aiohttp

from selenium import webdriver
from src.core.schemas.data import Article

logger = logging.getLogger(__name__)


class BeautifulSoupScraperBase:
    async def _fetch_html(self, session: aiohttp.ClientSession, url: str) -> str:
        logger.info(f"Fetching HTML content from URL: {url}")

        try:
            async with session.get(url) as response:
                response.raise_for_status()
                html_content = await response.text()
                logger.info("HTML content fetched successfully")
                return html_content

        except Exception as e:
            logger.info(f"An error occurred while fetching HTML: {e}")

            return ""

    async def _extract_data(self, html: str) -> list[Article]:
        raise NotImplementedError("Subclasses should implement this method")

    async def _write_data(self, articles: list[Article], filename: str) -> None:
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        async with aiofiles.open(filename, "w", encoding="utf-8") as file:
            await file.write(formatted_json)
            logger.info("Data written successfully")

    async def scrape(self, url: str, filename: str) -> None:
        async with aiohttp.ClientSession() as session:
            html = await self._fetch_html(session, url)
            articles = await self._extract_data(html)
            await self._write_data(articles, filename)

    async def apply_filters(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    async def scrape_page(self, session: aiohttp.ClientSession, url: str) -> list[Article]:
        html = await self._fetch_html(session, url)
        if html:
            return await self._extract_data(html)
        return []

    async def apply_filters(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses should implement this method")


class SeleniumScraperBase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.executor = ThreadPoolExecutor(max_workers=1)
        logger.info("Selenium WebDriver initialized")

    async def _fetch_html(self, session, url: str) -> str:
        logger.info(f"Navigating to URL using Selenium WebDriver: {url}")
        loop = asyncio.get_event_loop()

        await loop.run_in_executor(self.executor, self.driver.get, url)
        logger.info("Page loaded successfully")

        return self.driver.page_source

    async def _extract_data(self) -> list[Article]:
        raise NotImplementedError("Subclasses should implement this method")

    async def _write_data(self, articles: list[Article], filename: str) -> None:
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        async with aiofiles.open(filename, "w", encoding="utf-8") as file:
            await file.write(formatted_json)
            logger.info("Data written successfully")

    def close(self):
        logger.info("Closing Selenium WebDriver")
        self.driver.quit()

    async def apply_filters(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    async def scrape(self, url: str, filename: str) -> None:
        async with aiohttp.ClientSession() as session:
            html = await self._fetch_html(session, url)
            articles = await self._extract_data()
            await self._write_data(articles, filename)
