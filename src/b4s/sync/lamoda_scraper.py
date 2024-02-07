import logging

from bs4 import BeautifulSoup

from src.core.interface.scraper_interface import BeautifulSoupScraperBase
from src.core.schemas import Article

logger = logging.getLogger(__name__)


class LamodaScraperB4s(BeautifulSoupScraperBase):
    def _extract_data(self, html: str) -> list:
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

    def run(self, url: str, filename: str):
        html_content = self._fetch_html(url)
        articles_data = self._extract_data(html_content)
        self._write_data(articles_data, filename)
