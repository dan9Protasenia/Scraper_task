# OOP Web Scraper

This repository contains an object-oriented web scraper built with Python. It utilizes Selenium for web automation and Beautiful Soup (B4s) for parsing web pages. A common interface is defined using Python's `typing` module, and data is written to a file with the help of Pydantic models. The project also demonstrates the use of asynchronous operations for concurrent web page processing.

## Features

- Common interface for web scraping tasks using `typing.Protocol`.
- Synchronous and asynchronous web scrapers for various resources like Hacker News, The New York Times, and others.
- Data models defined with Pydantic for structured data output.
- Custom filter methods for pagination in scraping processes.
- Error handling and logging capabilities for robust and transparent operation.
- Poetry for dependency management and simplified project setup.

## Installation

Ensure you have Python 3.12 or above installed on your system.

1. Clone the repository:
   ```sh
   git clone https://github.com/dan9Protasenia/Scraper_task
   cd scraper_task
   ```

2. Install Poetry if it's not already installed:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install project dependencies using Poetry:
   ```sh
   poetry install
   ```

## Usage

The project includes both synchronous and asynchronous scrapers. To start a scraping task, use the following commands:

- For synchronous scraping:
  ```sh
  poetry run python -m src.main [scraper_flag]
  ```
  Replace `[scraper_flag]` with `nyt`, `hack`, `rabota`, `hh`, or `lamoda_sel` to select the respective scraper.

- For asynchronous scraping:
  ```sh
  poetry run python -m src.main_async [scraper_flag]
  ```
  Replace `[scraper_flag]` with `nyt`, `hh`, `rabota`, `hack`, `lamoda_b4s`, or `lamoda_sel` to select the respective scraper.

Note: You can specify multiple flags to run several scrapers in sequence.

## Project Structure

- `src/`: Main source code directory.
  - `b4s/`: Contains Beautiful Soup scrapers.
  - `core/`: Core interfaces and shared modules.
  - `selenium/`: Selenium-based scrapers.
  - `main.py`: Entry point for synchronous scraping.
  - `main_async.py`: Entry point for asynchronous scraping.
- `Dockerfile`: Configuration for Docker containerization.
- `poetry.lock` and `pyproject.toml`: Poetry configuration and dependency files.

## Docker Support

To build a Docker image for the project, run:

```sh
docker build -t scraper_task .
```

To run a scraper inside a Docker container, use:

```sh
docker run scraper_task [scraper_flag]
```

## Contributing

Please read the task guidelines in `task.md` for details on the code style, commit messages, and branch workflow. Contributions are welcome through pull requests to the repository.

## License

This project is licensed under the MIT License

