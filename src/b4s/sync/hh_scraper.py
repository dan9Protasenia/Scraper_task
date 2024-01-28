from typing import Any

from bs4 import BeautifulSoup

from src.core.interface.scraper_interface import BeautifulSoupScraperBase
from src.core.schemas import Article


class HhScraper(BeautifulSoupScraperBase):
    def _extract_data(self, html: str) -> list[Any]:
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

    def run(self, url: str, filename: str):
        html_content = self._fetch_html(url)
        articles_data = self._extract_data(html_content)
        self._write_data(articles_data, filename)
