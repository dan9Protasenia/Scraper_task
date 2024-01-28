from typing import Any

from selenium.webdriver.common.by import By
from src.core.interface.scraper_interface import SeleniumScraperBase
from src.core.schemas.data import Article


class RabotaScraper(SeleniumScraperBase):
    def _extract_data(self) -> list[Any]:
        posts_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.bloko-link")

        data = []

        for post in posts_elements:
            link = post.get_attribute("href")
            title = post.text

            if title and link and "/vacancy/" in link:
                article = Article(title=title, link=link)
                data.append(article)

        return data

    def run(self, url: str, filename: str):
        self.initialize_scraper()
        self.navigate_to_page(url)
        data = self._extract_data()
        self._write_data(data, filename)
        self.driver.quit()
