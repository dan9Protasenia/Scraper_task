from typing import List

from bs4 import BeautifulSoup

from src.core.interface.scraper_interface_async import BeautifulSoupScraperBase
from src.core.schemas.data import Article


class HhScraperAsync(BeautifulSoupScraperBase):
    async def _extract_data(self, html: str) -> List[Article]:
        soup = BeautifulSoup(html, "html.parser")
        posts_elements = soup.select("a.bloko-link")

        data = []
        for post in posts_elements:
            link = post.get("href")
            title = post.get_text()

            if title and link and "/vacancy/" in link:
                article = Article(title=title, link=link)
                data.append(article)

        return data
