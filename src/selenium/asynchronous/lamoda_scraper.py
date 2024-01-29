import asyncio
import logging
from typing import Any

import aiofiles
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.core.interface.scraper_interface import SeleniumScraperBase
from src.core.schemas.data import Article
import json

logger = logging.getLogger(__name__)


class LamodaScraperSeleniumAsync(SeleniumScraperBase):

    def __init__(self):
        self.driver = None
        logger.info("WebScraperInterface initialized")

    async def initialize_scraper(self):
        if self.driver is not None:
            self.driver.quit()
            logger.info("Quitting existing WebDriver instance")
        self.driver = webdriver.Chrome()
        logger.info("WebDriver Chrome initialized")

    async def navigate_to_page(self, url: str):
        logger.info(f"Navigating to page: {url}")
        self.driver.get(url)

    async def _extract_data(self) -> list[Any]:
        data = []

        product_cards = self.driver.find_elements(By.CSS_SELECTOR, ".x-product-card__card")
        logger.info(f"Product cards found: {len(product_cards)}")

        for index, card in enumerate(product_cards):
            link_element = card.find_element(By.CSS_SELECTOR, "a")
            brand_element = card.find_element(By.CSS_SELECTOR, ".x-product-card-description__brand-name")
            product_name_element = card.find_element(By.CSS_SELECTOR, ".x-product-card-description__product-name")

            title = None
            if brand_element and product_name_element:
                title = brand_element.text.strip() + ' ' + product_name_element.text.strip()
            else:
                logger.warning(f"Card {index + 1}: The product name was not found")

            link = link_element.get_attribute("href")

            if link and title:
                article = Article(title=title, link=link)
                data.append(article)

            else:
                logger.warning(f"Card {index + 1}: The data is incomplete")

        return data

    async def _write_data(self, articles: list[Article], filename: str) -> None:
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        async with aiofiles.open(filename, "w", encoding="utf-8") as file:
            await file.write(formatted_json)
            logger.info("Data written successfully")

    async def run(self, url: str, filename: str, max_pages: int = 10):
        await self.initialize_scraper()
        all_articles = []

        async def fetch_page_data(page_number):
            page_url = f"{url}{page_number}"
            logger.info(f"Fetching data from page: {page_url}")
            await self.navigate_to_page(page_url)
            articles = await self._extract_data()
            return articles

        tasks = [fetch_page_data(page_number) for page_number in range(1, max_pages + 1)]
        pages_data = await asyncio.gather(*tasks)

        for articles in pages_data:
            all_articles.extend(articles)

        await self._write_data(all_articles, filename)
        self.driver.quit()
