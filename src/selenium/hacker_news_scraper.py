from src.core.scraper_interface import WebScraperInterface


class HackerNewsScraper(WebScraperInterface):
    def initialize_scraper(self):
        pass

    def navigate_to_page(self, url: str):
        pass

    def extract_data(self):
        pass

    def write_data(self, data, filename: str):
        pass

    def apply_filters(self, **kwargs):
        pass
