import asyncio
import logging
from typing import Any, List

import aiohttp
from bs4 import BeautifulSoup

from src.core.interface.scraper_interface_async import BeautifulSoupScraperBase
from src.core.schemas.data import Article

logger = logging.getLogger(__name__)


class LamodaScraperAsync(BeautifulSoupScraperBase):
    async def _extract_data(self, html: str) -> List[Article]:
        soup = BeautifulSoup(html, "html.parser")
        product_cards = soup.select(".x-product-card__card")
        logger.info(f"Product cards found: {len(product_cards)}")

        articles = []

        for index, card in enumerate(product_cards):
            link_element = card.select_one("a")
            brand_element = card.select_one(".x-product-card-description__brand-name")
            product_name_element = card.select_one(".x-product-card-description__product-name")

            title = None
            if brand_element and product_name_element:
                title = f"{brand_element.text.strip()} {product_name_element.text.strip()}"
            else:
                logger.warning(f"Card {index + 1}: The product name was not found")

            link = link_element["href"] if link_element else None

            if link and title:
                article = Article(title=title, link=link)
                articles.append(article)
            else:
                logger.warning(f"Card {index + 1}: The data is incomplete")

        return articles

    async def scrape(self, base_url: str, filename: str, max_pages: int = 200) -> None:
        async with aiohttp.ClientSession() as session:
            tasks = [self.scrape_page(session, f"{base_url}?page={i}") for i in range(1, max_pages + 1)]
            pages_articles = await asyncio.gather(*tasks)
            articles = [article for page in pages_articles for article in page]
            await self._write_data(articles, filename)