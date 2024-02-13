from selenium.webdriver.common.by import By
from src.core.interface.scraper_interface_async import SeleniumScraperBase
from src.core.schemas.data import Article


class RabotaScraperAsync(SeleniumScraperBase):
    async def _extract_data(self) -> list[Article]:
        posts_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.bloko-link")

        data = []
        for post in posts_elements:
            link = post.get_attribute("href")
            title = post.text

            if title and link and "/vacancy/" in link:
                article = Article(title=title, link=link)
                data.append(article)

        return data
