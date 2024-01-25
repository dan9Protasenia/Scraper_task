import json
from typing import Any, Protocol

import requests

from selenium import webdriver


class WebScraperInterface(Protocol):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def initialize_scraper(self):
        self.driver = webdriver.Chrome()

    def fetch_html(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)

        response.raise_for_status()
        return response.text

    def navigate_to_page(self, url: str):
        self.driver.get(url)

    def extract_data(self) -> Any:
        ...

    def write_data(self, articles: list, filename: str) -> None:
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(formatted_json)

    def apply_filters(self, **kwargs) -> None:
        ...
