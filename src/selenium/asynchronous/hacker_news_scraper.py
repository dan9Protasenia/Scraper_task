from selenium.webdriver.common.by import By

from ...core.schemas.data import Article
from ...scraper_interface_async import WebScraperInterfaceAsync


class HackerNewsScraperAsync(WebScraperInterfaceAsync):
    async def extract_data(self, html: str):
        posts_elements = self.driver.find_elements(By.CSS_SELECTOR, "tr.athing .title a")
        data = []

        for post in posts_elements:
            link = post.get_attribute("href")
            title = post.text

            if title and link in link and not link.startswith("https://news.ycombinator.com/from?site="):
                article = Article(title=title, link=link)
                data.append(article)

        return data

    async def apply_filters(self, **kwargs):
        ...
