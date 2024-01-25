import asyncio
import logging
import sys

from .b4s.asynchronous.hh_scraper import HhScraperAsync
from .b4s.asynchronous.nyt_scraper import NYTimesScraperAsync

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


async def main():
    if len(sys.argv) > 1:
        if "hh_async" in sys.argv:
            logger.info("Starting HH Scraper (Async)")
            url = (
                "https://hh.ru/search/vacancy?L_save_area=true&text=python&excluded"
                "_text=&area=1002&salary=&currency_code=RUR&experience=doesNotMatter"
                "&order_by=relevance&search_period=0&items_on_page=50"
            )

            filename = "hh_data_async.json"
            scraper = HhScraperAsync()

            await scraper.scrape(url, filename)
            logger.info("HH Scraper (Async) completed")

        if "nyt_async" in sys.argv:
            logger.info("Starting NYT Scraper (Async)")
            url = "https://www.nytimes.com"

            filename = "nyt_data_async.json"
            scraper = NYTimesScraperAsync()

            await scraper.scrape(url, filename)
            logger.info("NYT Scraper (Async) completed")


if __name__ == "__main__":
    asyncio.run(main())
