from Scraper_task.src.core.schemas.data import Article
from Scraper_task.src.scraper_interface import WebScraperInterface
from selenium.webdriver.common.by import By


class HackerNewsScraper(WebScraperInterface):
    def extract_data(self):
        posts_elements = self.driver.find_elements(By.CSS_SELECTOR, "tr.athing .title a")
        data = []
        for post in posts_elements:
            link = post.get_attribute("href")
            if not link.startswith("https://news.ycombinator.com/from?site="):
                article = Article(title=post.text, link=link)
                data.append(article)
        return data

    def apply_filters(self, **kwargs):
        ...
