from selenium.webdriver.common.by import By
from src.core.interface.scraper_interface import SeleniumScraperBase
from src.core.schemas.data import Article


class HackerNewsScraper(SeleniumScraperBase):
    def _extract_data(self) -> list:
        posts_elements = self.driver.find_elements(By.CSS_SELECTOR, "tr.athing .title a")

        data = []

        for post in posts_elements:
            link = post.get_attribute("href")
            if not link.startswith("https://news.ycombinator.com/from?site="):
                article = Article(title=post.text, link=link)
                data.append(article)
        return data

    def run(self, url: str, filename: str):
        self.initialize_scraper()
        self.navigate_to_page(url)
        data = self._extract_data()
        self._write_data(data, filename)
        self.driver.quit()
