import asyncio
import sys

# sync
from .b4s.sync.hh_scraper import HhScraper
from .b4s.sync.nyt_scraper import NYTimesScraperBS
from .selenium.sync.hacker_news_scraper import HackerNewsScraper
from .selenium.sync.rabota_scraper import RabotaScraper


def main():
    if len(sys.argv) > 1:
        if "nyt" in sys.argv:
            print("Starting NYT scraper...")
            url = "https://www.nytimes.com"
            scraper = NYTimesScraperBS()
            print(f"Fetching HTML content for {url}")
            html_content = scraper.fetch_html(url)
            print("Extracting data...")
            articles_data = scraper.extract_data(html_content)
            print(f"Extracted {len(articles_data)} articles")
            print("Writing data to file...")
            scraper.write_data(articles_data, "nyt_data.json")
            print("NYT data scraping and writing complete.")

        if "hack" in sys.argv:
            print("Starting Hacker News scraper...")
            scraper = HackerNewsScraper()
            scraper.initialize_scraper()
            scraper.navigate_to_page("https://news.ycombinator.com/")
            data = scraper.extract_data()
            scraper.write_data(data, "hacker_news_data.json")
            scraper.driver.quit()
            print("Hacker News data scraping and writing complete.")

        if "rabota" in sys.argv:
            print("Starting Rabota scraper...")
            scraper = RabotaScraper()
            scraper.initialize_scraper()
            scraper.navigate_to_page(
                "https://rabota.by/search/vacancy?L_save_area=true&text=Python&excluded_text=&area"
                "=1002&salary=&currency_code=BYR&experience=doesNotMatter&order_by=relevance&search"
                "_period=0&items_on_page=50"
            )
            data = scraper.extract_data()
            scraper.write_data(data, "rabota_data.json")
            scraper.driver.quit()
            print("Rabota scraping and writing complete.")

        if "hh" in sys.argv:
            print("Starting HH scraper...")
            url = (
                "https://hh.ru/search/vacancy?L_save_area=true&text=python&excluded_text=&area=10"
                "02&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_"
                "period=0&items_on_page=50"
            )
            scraper = HhScraper()
            print(f"Fetching HTML content for {url}")
            html_content = scraper.fetch_html(url)
            print("Extracting data...")
            articles_data = scraper.extract_data(html_content)
            print(f"Extracted {len(articles_data)} articles")
            print("Writing data to file...")
            scraper.write_data(articles_data, "hh_data.json")
            print("HH data scraping and writing complete.")


if __name__ == "__main__":
    main()
