import logging

from bs4 import BeautifulSoup

from src.core.interface.scraper_interface_async import BeautifulSoupScraperBase
from src.core.schemas.data import Article

logger = logging.getLogger(__name__)


class NYTimesScraperAsync(BeautifulSoupScraperBase):
    async def _extract_data(self, html: str) -> list[Article]:
        soup = BeautifulSoup(html, "html.parser")
        article_sections = soup.select("section.story-wrapper")

        data = []

        for section in article_sections:
            try:
                link_element = section.select_one('a[class*="css-"]')

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

            except (AttributeError, TypeError):
                logger.exception("Error extracting data from section", exc_info=e)
                continue

        return data
