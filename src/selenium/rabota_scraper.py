from selenium.webdriver.common.by import By

from ..core.schemas.data import Article
from ..scraper_interface import WebScraperInterface


class RabotaScraper(WebScraperInterface):
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

    def apply_filters(self, **kwargs):
        ...
