import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from ..core.scraper_interface import WebScraperInterface


class HackerNewsScraper(WebScraperInterface):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def initialize_scraper(self):
        self.driver = webdriver.Chrome()

    def navigate_to_page(self, url: str):
        self.driver.get(url)

    def extract_data(self):
        posts = self.driver.find_elements(By.CSS_SELECTOR, "tr.athing .title a")
        data = []
        for post in posts:
            link = post.get_attribute("href")
            if not link.startswith("https://news.ycombinator.com/from?site="):
                data.append({"title": post.text, "link": link})
        return data

    def write_data(self, data, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def apply_filters(self, **kwargs):
        ...
