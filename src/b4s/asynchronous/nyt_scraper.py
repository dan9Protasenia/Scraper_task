from typing import List

from bs4 import BeautifulSoup

from ...core.schemas.data import Article
from ...scraper_interface_async import WebScraperInterfaceAsync


class NYTimesScraperAsync(WebScraperInterfaceAsync):
    async def extract_data(self, html: str) -> List[Article]:
        soup = BeautifulSoup(html, "html.parser")
        article_sections = soup.select("section.story-wrapper")

        data = []
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
