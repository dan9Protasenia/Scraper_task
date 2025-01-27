import asyncio
import logging
import sys

from src.b4s.asynchronous.hh_scraper import HhScraperAsync
from src.b4s.asynchronous.lamoda_scraper import LamodaScraperAsync
from src.b4s.asynchronous.nyt_scraper import NYTimesScraperAsync
from src.logger_config import setup_logging
from src.selenium.asynchronous.hacker_news_scraper import HackerNewsScraperAsync
from src.selenium.asynchronous.lamoda_scraper import LamodaScraperSeleniumAsync
from src.selenium.asynchronous.rabota_scraper import RabotaScraperAsync

logger = logging.getLogger(__name__)


async def run_hh_scraper():
    url = (
        "https://hh.ru/search/vacancy?L_save_area=true&text=python&excluded"
        "_text=&area=1002&salary=&currency_code=RUR&experience=doesNotMatter"
        "&order_by=relevance&search_period=0&items_on_page=50"
    )

    filename = "hh_data_async.json"
    scraper = HhScraperAsync()

    await scraper.scrape(url, filename)


async def run_lamoda_scraper_b4s():
    url = "https://www.lamoda.ru/c/355/clothes-zhenskaya-odezhda/?page="
    filename = "lamoda_data_async.json"
    scraper = LamodaScraperAsync()

    try:
        await scraper.scrape(url, filename)
        logger.info("Scraping completed successfully")

    except Exception as e:
        logger.error(f"An error occurred during scraping: {e}", exc_info=True)

    finally:
        logger.info("Scraper closed and resources released")


async def run_lamoda_scraper_selenium():
    url = "https://www.lamoda.ru/c/355/clothes-zhenskaya-odezhda/?page="
    filename = "lamoda_data_async.json"
    scraper = LamodaScraperSeleniumAsync()

    try:
        await scraper.scrape(url, filename)
        logger.info("Scraping completed successfully")

    except Exception as e:
        logger.error(f"An error occurred during scraping: {e}", exc_info=True)

    finally:
        logger.info("Scraper closed and resources released")


async def run_nyt_scraper():
    url = "https://www.nytimes.com"

    filename = "nyt_data_async.json"
    scraper = NYTimesScraperAsync()

    await scraper.scrape(url, filename)


async def run_rabota_scraper():
    url = (
        "https://rabota.by/search/vacancy?L_save_area=true&text=Python&excluded"
        "_text=&area=1002&salary=&currency_code=BYR&experience=doesNotMatter&or"
        "der_by=relevance&search_period=0&items_on_page=50"
    )

    filename = "rabota_data_async.json"
    scraper = RabotaScraperAsync()

    try:
        await scraper.scrape(url, filename)
        logger.info("Scraping completed successfully")

    except Exception as e:
        logger.error(f"An error occurred during scraping: {e}", exc_info=True)

    finally:
        scraper.close()
        logger.info("Scraper closed and resources released")


async def run_hack_scraper():
    logger.info("Starting Hacker Scraper (Async)")
    url = "https://news.ycombinator.com/"

    filename = "hack_data_async.json"
    scraper = HackerNewsScraperAsync()

    try:
        await scraper.scrape(url, filename)
        logger.info("Scraping completed successfully")

    except Exception as e:
        logger.error(f"An error occurred during scraping: {e}", exc_info=True)

    finally:
        scraper.close()
        logger.info("Scraper closed and resources released")


async def main():
    if len(sys.argv) > 1:
        scraper_run = False
        if "nyt" in sys.argv:
            await run_nyt_scraper()
            scraper_run = True
        if "hh" in sys.argv:
            await run_hh_scraper()
            scraper_run = True
        if "rabota" in sys.argv:
            await run_rabota_scraper()
            scraper_run = True
        if "hack" in sys.argv:
            await run_hack_scraper()
            scraper_run = True
        if "lamoda_b4s" in sys.argv:
            await run_lamoda_scraper_b4s()
            scraper_run = True
        if "lamoda_sel" in sys.argv:
            await run_lamoda_scraper_selenium()
            scraper_run = True
        if not scraper_run:
            logger.warning("The specified argument is not supported.")
    else:
        logger.warning("No arguments were entered. Please provide an argument to start the scraper.")


if __name__ == "__main__":
    setup_logging()
    asyncio.run(main())
