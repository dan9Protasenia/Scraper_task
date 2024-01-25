from typing import List

from bs4 import BeautifulSoup

from ...core.schemas.data import Article
from ...scraper_interface_async import WebScraperInterfaceAsync


class HhScraperAsync(WebScraperInterfaceAsync):

    async def extract_data(self, html: str) -> List[Article]:
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
