import sys

from .b4s.nyt_scraper import NYTimesScraperBS
from .selenium.hacker_news_scraper import HackerNewsScraper


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "nyt":
        print("Starting NYT scraper...")
        url = "https://www.nytimes.com"

        scraper = NYTimesScraperBS()
        print(f"Fetching HTML content for {url}")

        html_content = scraper.fetch_html(url)
        print("Extracting data...")

        articles_data = scraper.extract_data(html_content)
        print(f"Extracted {len(articles_data)} articles")

        print("Writing data to file...")
        scraper.write_data(articles_data, "nyt_articles.json")

        print("NYT data scraping and writing complete.")

    elif len(sys.argv) > 1 and sys.argv[1] == "hack":
        print("Starting Hacker News scraper...")
        scraper = HackerNewsScraper()
        scraper.initialize_scraper()
        scraper.navigate_to_page("https://news.ycombinator.com/")
        data = scraper.extract_data()
        scraper.write_data(data, "hacker_news_data.json")
        scraper.driver.quit()
        print("Hacker News data scraping and writing complete.")


if __name__ == "__main__":
    main()
