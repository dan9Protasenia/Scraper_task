import logging
import sys

from src.b4s.sync.hh_scraper import HhScraper
from src.b4s.sync.nyt_scraper import NYTimesScraperBS
from src.logger_config import setup_logging
from src.selenium.sync.hacker_news_scraper import HackerNewsScraper
from src.selenium.sync.lamoda_scraper import LamodaScraperSelenium
from src.selenium.sync.rabota_scraper import RabotaScraper

logger = logging.getLogger(__name__)


def run_nyt_scraper():
    url = "https://www.nytimes.com"
    filename = "nyt_data.json"
    scraper = NYTimesScraperBS()
    scraper.run(url, filename)


def run_lamoda_scraper():
    url = f"https://www.lamoda.ru/c/355/clothes-zhenskaya-odezhda/?sitelink=topmenuW&l=3&page="
    scraper = LamodaScraperSelenium()
    filename = "lamoda_data.json"
    scraper.run(url, filename)


def run_hh_scraper():
    url = (
        "https://hh.ru/search/vacancy?L_save_area=true&text=python&excluded_text=&area=10"
        "02&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_"
        "period=0&items_on_page=50"
    )
    scraper = HhScraper()
    filename = "hh_data.json"
    scraper.run(url, filename)


def run_hacker_news_scraper():
    url = "https://news.ycombinator.com/"
    filename = "hacker_news_data.json"
    scraper = HackerNewsScraper()
    scraper.run(url, filename)


def run_rabota_scraper():
    url = (
        "https://rabota.by/search/vacancy?L_save_area=true&text=Python&excluded_text=&area"
        "=1002&salary=&currency_code=BYR&experience=doesNotMatter&order_by=relevance&search"
        "_period=0&items_on_page=50"
    )
    filename = "rabota_data.json"
    scraper = RabotaScraper()
    scraper.run(url, filename)


def main():
    if len(sys.argv) > 1:
        scraper_run = False
        if "nyt" in sys.argv:
            run_nyt_scraper()
            scraper_run = True
        if "hack" in sys.argv:
            run_hacker_news_scraper()
            scraper_run = True
        if "rabota" in sys.argv:
            run_rabota_scraper()
            scraper_run = True
        if "hh" in sys.argv:
            run_hh_scraper()
            scraper_run = True
        if "lamoda_sel" in sys.argv:
            run_lamoda_scraper()
            scraper_run = True
        # if "lamoda_b4s" in sys.argv:
        #     run_lamoda_scraper_b4s()
        # scraper_run = True
        if not scraper_run:
            logger.warning("The specified argument is not supported.")
    else:
        logger.warning("No arguments were entered. Please provide an argument to start the scraper.")


if __name__ == "__main__":
    setup_logging()
    main()
