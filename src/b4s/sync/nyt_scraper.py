import logging
from typing import Any

from bs4 import BeautifulSoup

from src.core.interface.scraper_interface import BeautifulSoupScraperBase
from src.core.schemas import Article

logger = logging.getLogger(__name__)


class NYTimesScraperBS(BeautifulSoupScraperBase):
    def _extract_data(self, html: str) -> list[Any]:
        soup = BeautifulSoup(html, "html.parser")
        posts_elements = soup.select("section.story-wrapper")

        data = []

        for posts in posts_elements:
            try:
                link_element = posts.select_one('a[class*="css-"]')

                if link_element is None:
                    logger.error("Missing link element in section")
                    continue

                title_element = link_element.select_one('p[class*="css-"]')

                if title_element is None:
                    logger.error("Missing title element in section")
                    continue

                title = title_element.get_text(strip=True)
                link = link_element["href"]

                if title and link:
                    data.append(Article(title=title, link=link))
                    logger.info(f"Article extracted: {title}")
                else:
                    logger.error("Article title or link is empty")

            except (AttributeError, TypeError) as e:
                logger.exception("Error extracting data from section", exc_info=e)
                continue

        logger.info(f"Total articles extracted: {len(data)}")
        return data

    def run(self, url: str, filename: str):
        html_content = self._fetch_html(url)
        articles_data = self._extract_data(html_content)
        self._write_data(articles_data, filename)
