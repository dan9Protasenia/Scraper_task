import json
import logging
from typing import Any
from src.logger_config import setup_logging
import requests
from bs4 import BeautifulSoup

from src.core.interface.scraper_interface import BeautifulSoupScraperBase
from src.core.schemas import Article

logger = logging.getLogger(__name__)


class LamodaScraper(BeautifulSoupScraperBase):
    def _extract_data(self, html: str) -> list[Any]:
        soup = BeautifulSoup(html, "html.parser")
        product_cards = soup.select(".x-product-card__card")
        logger.info(f"Product cards found: {len(product_cards)}")

        data = []
        for index, card in enumerate(product_cards):
            link_element = card.select_one(".x-product-card__link")
            brand_element = card.select_one(".x-product-card-description__brand-name")
            product_name_element = card.select_one(".x-product-card-description__product-name")

            title = None
            if brand_element and product_name_element:
                title = brand_element.get_text(strip=True) + ' ' + product_name_element.get_text(strip=True)
                logger.info(f"Card {index + 1}: Product name - {title}")
            else:
                logger.warning(f"Card {index + 1}: The product name was not found")

            link = link_element.get("href") if link_element else None

            if link and title:
                article = Article(title=title, link=link)
                data.append(article)
            else:
                logger.warning(f"Card {index + 1}: The data is incomplete")

        return data

    def _fetch_html(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        logger.info(f"Fetching HTML from URL: {url}")
        response = requests.get(url, headers=headers)

        response.raise_for_status()
        logger.info("HTML fetched successfully")

        return response.text

    def _write_data(self, articles: list, filename: str) -> None:
        logger.info(f"Writing data to {filename}")
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(formatted_json)
            logger.info("Data written successfully")

    def run(self, url: str, filename: str, max_pages: int = 10):
        all_articles = []
        for page_number in range(1, max_pages + 1):
            page_url = f"{url}&page={page_number}"
            logger.info(f"Fetching data from page: {page_url}")
            page_content = self._fetch_html(page_url)
            articles = self._extract_data(page_content)
            all_articles.extend(articles)

        self._write_data(all_articles, filename)


def run_lamoda_scraper(page_num):
    url = (
        f"https://stopgame.ru/topgames?p={page_num}"
    )
    scraper = LamodaScraper()
    filename = "stopgame.json"
    max_pages = 1  # Установите максимальное количество страниц для сканирования
    scraper.run(url, filename, max_pages)


def main():
    page_num = 1
    run_lamoda_scraper(page_num)


if __name__ == "__main__":
    setup_logging()
    main()
