import json

import requests
from bs4 import BeautifulSoup

from ..core.schemas.data import Article


class NYTimesScraperBS:
    def fetch_html(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

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

    def write_data(self, articles: list, filename: str):
        articles_data = [article.dict() for article in articles]
        formatted_json = json.dumps(articles_data, ensure_ascii=False, indent=4)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(formatted_json)
