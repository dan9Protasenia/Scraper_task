from bs4 import BeautifulSoup

from ..core.schemas.data import Article
from ..scraper_interface import WebScraperInterface


class NYTimesScraperBS(WebScraperInterface):
    def extract_data(self, html: str) -> list:
        soup = BeautifulSoup(html, "html.parser")
        data = []

        article_sections = soup.select("section.story-wrapper")

        for section in article_sections:
            try:
                link_element = section.select_one('a[class*="css-"]')
                title_element = link_element.select_one('p[class*="css-"]')
                title = title_element.get_text(strip=True)
                link = link_element["href"]

                if title and link:
                    data.append(Article(title=title, link=link))
            except (AttributeError, TypeError):
                continue

        return data
