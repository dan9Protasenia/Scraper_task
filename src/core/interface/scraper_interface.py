import json
import logging

import requests

from selenium import webdriver

logger = logging.getLogger(__name__)


class BeautifulSoupScraperBase:
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

    def _extract_data(self, html: str) -> list:
        raise NotImplementedError("Subclasses should implement this method")

    def _write_data(self, articles: list, filename: str) -> None:
        logger.info(f"Writing data to {filename}")
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(formatted_json)
            logger.info("Data written successfully")

    def apply_filters(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses should implement this method")


class SeleniumScraperBase:
    def __init__(self):
        self.driver = None
        logger.info("WebScraperInterface initialized")

    def initialize_scraper(self):
        if self.driver is not None:
            self.driver.quit()
            logger.info("Quitting existing WebDriver instance")
        self.driver = webdriver.Chrome()
        logger.info("WebDriver Chrome initialized")

    def navigate_to_page(self, url: str):
        logger.info(f"Navigating to page: {url}")
        self.driver.get(url)

    def _extract_data(self) -> list:
        raise NotImplementedError("Subclasses should implement this method")

    def _write_data(self, articles: list, filename: str) -> None:
        logger.info(f"Writing data to {filename}")
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(formatted_json)
            logger.info("Data written successfully")

    def apply_filters(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses should implement this method")
