import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from ..core.schemas.data import Article
from ..scraper_interface import WebScraperInterface


class HhScraper(WebScraperInterface):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def initialize_scraper(self):
        self.driver = webdriver.Chrome()

    def navigate_to_page(self, url: str):
        self.driver.get(url)

    def extract_data(self):
        posts_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.bloko-link")

        data = []
        for post in posts_elements:
            link = post.get_attribute("href")
            title = post.text

            if title and link and "/vacancy/" in link:
                article = Article(title=title, link=link)
                data.append(article)

        return data

    def write_data(self, articles: list, filename: str):
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(formatted_json)

    def apply_filters(self, **kwargs):
        ...
