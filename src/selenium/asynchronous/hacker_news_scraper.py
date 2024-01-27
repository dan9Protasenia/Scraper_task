from typing import List

from selenium.webdriver.common.by import By
from src.core.interface.scraper_interface_async import SeleniumScraperBase
from src.core.schemas.data import Article


class HackerNewsScraperAsync(SeleniumScraperBase):
    async def _extract_data(self) -> List[Article]:
        posts_elements = self.driver.find_elements(By.CSS_SELECTOR, "tr.athing .title a")

        data = []
        for post in posts_elements:
            link = post.get_attribute("href")
            title = post.text

            if title and link in link and not link.startswith("https://news.ycombinator.com/from?site="):
                article = Article(title=title, link=link)
                data.append(article)

        return data
