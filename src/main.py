from .selenium.hacker_news_scraper import HackerNewsScraper


def main():
    scraper = HackerNewsScraper()

    scraper.initialize_scraper()

    scraper.navigate_to_page("https://news.ycombinator.com/")

    data = scraper.extract_data()

    scraper.write_data(data, "hacker_news_data.json")

    scraper.driver.quit()

    print("Data scraping and writing complete.")


if __name__ == "__main__":
    main()
