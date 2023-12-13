# OOP Web Scraper on Python

## Objective:
Develop a web scraper in Python using the Selenium framework, define a common interface using the `typing` module, and use Pydantic to write scraped data to a file. Additionally, implement filter methods for dates, pagination, and an asynchronous parser.

### Requirements:
1. **Common Interface:**
   - Define a common interface for the web scraper using `protocol` from the `typing` module.
   - The interface should include methods for initializing the scraper, navigating to a webpage, extracting data from the webpage, writing the data to a file, and incorporating filter methods for dates and pagination.

2. **Selenium Web Scraper:**
   - Implement a web scraper class that adheres to the defined interface.
   - Use the Selenium framework for web automation.
   - The scraper should be able to:
      - Initialize a Selenium WebDriver.
      - Navigate to a specified webpage.
      - Extract information from the webpage (e.g., text, links, images).
      - Write the extracted data to a file.
      - Include filter methods for date ranges and pagination.

3. **Pydantic Data Models:**
   - Define Pydantic data models to represent the structure of the scraped data.
   - Ensure the data models cover the relevant information extracted from the webpage.

4. **Asynchronous Parser:**
   - Implement an asynchronous parser for processing web pages concurrently.
   - Demonstrate the use of asynchronous functions, `asyncio`, and the `aiohttp` library.

5. **Usage Example:**
   - Provide a simple usage example demonstrating the initialization of the scraper, navigation to a webpage, extraction of information, writing the data to a file using Pydantic, and applying filter methods.

### Additional Challenges (Optional):
1. **Customization:**
   - Allow customization of the Selenium WebDriver options, such as specifying the browser type, headless mode, etc.

2. **Error Handling:**
   - Implement error handling for common scenarios, such as invalid URLs, element not found, or WebDriver initialization failure.

3. **Logging:**
   - Implement logging to capture relevant information and errors during scraping.

4. **Unit Tests:**
   - Write unit tests for the main functionality of the web scraper.

### Submission:
- Submit the codebase along with a brief README explaining how to use the web scraper, any additional features implemented, and any challenges faced.

### Note:
- You are free to use any additional libraries or tools you find suitable for the task.
- Make sure to adhere to best practices in terms of code readability, structure, and documentation also dont forget about PEP8.
- Use Python 3.10 or above.
- Use poetry as dependency manager and config storage.
- Add popular linters and formattetes.

### Proposed project structure:
```
./
├── src/
│   ├── core/
│   │   └── __init__.py
│   ├── working_parser_1/
│   │   └── __init__.py
│   ├── working_parser_2/
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
├── .env
├── .env.example
├── .gitignore
├── README.md
└── task.md
```
