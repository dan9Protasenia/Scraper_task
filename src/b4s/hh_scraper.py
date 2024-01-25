from bs4 import BeautifulSoup

from ..core.schemas.data import Article
from ..scraper_interface import WebScraperInterface


class HhScraper(WebScraperInterface):
    def extract_data(self, html: str):
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

    def apply_filters(self, **kwargs):
        ...
