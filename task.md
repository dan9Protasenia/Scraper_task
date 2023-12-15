# OOP Web Scraper


## Objective:
Develop a web scraper in Python using the `Selenium` framework and `B4s`, define a common interface using the `typing` module, and use `Pydantic` to write scraped data to a file. Additionally, implement filter methods for dates, pagination, and an asynchronous parser.


### Requirements:
1. **Poetry:**
    - Use Poetry for managing Python dependencies.
    - Add popular linters and add configs there.

2. **Common Interface:**
    - Define a common interface for the web scraper using `protocol` from the `typing` module.
    - The interface should include methods for initializing the scraper, navigating to a webpage, extracting data from the webpage, writing the data to a file, and incorporating filter methods for dates and pagination.

3. **Selenium Web Scraper:**
    - Resources to scrap:
      + Hacker news
      + NYT
      + _this one is up to you_
    - Implement a web scraper class that adheres to the defined interface.
    - Use the `Selenium` framework for web automation.
    - The scraper should be able to:
      + Initialize a Selenium WebDriver.
      + Navigate to a specified webpage.
      + Extract information from the webpage (e.g., text, links, images).
      + Write the extracted data to a file.
      + Include filter methods for date ranges and pagination.

4. **Pydantic Data Models:**
    - Define `Pydantic` data models to represent the structure of the scraped data.
    - Ensure the data models cover the relevant information extracted from the webpage.

5. **Asynchronous Scraper:**
    - First of all try to make sync scraper.
    - Implement an asynchronous parser for processing web pages concurrently.
    - Demonstrate the use of asynchronous functions, `asyncio`, and the `aiohttp` library.

6. **Usage Example:**
    - Provide a simple usage example demonstrating the initialization of the scraper, navigation to a webpage, extraction of information, writing the data to a file using `Pydantic`, and applying filter methods.


### Additional Challenges (Optional):
1. **Customization:**
   - Allow customization of the `Selenium` WebDriver options, such as specifying the browser type, headless mode, etc.

2. **Error Handling:**
   - Implement error handling for common scenarios, such as invalid URLs, element not found, or WebDriver initialization failure.

3. **Logging:**
   - Implement logging to capture relevant information and errors during scraping.

4. **Unit Tests:**
   - Write unit tests using `pytest` for the main functionality of the web scraper using `pytest`.

5. **Beautiful Soup:**
   - Write other simple scraper using `Beautiful Soup` which will use the same interfaces.


### Submission:
- All Python code **MUST** be _typed_ (the `typing` module to your rescue).
- Implement the project according to the `PEP8` standard should be described in the `tool` section of the _pyproject.toml_ for linters with some modifications:
    + String length should be 120 characters.
    + Count of lines after import should be 2.
    + The rest is by specification.
- `Pytest` should be in in the `tool` section of the _pyproject.toml_.
- Commit style, [click](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/). Commits should contain small logical portions of the code being modified. A clear commit name is required, descriptions within commits are welcome. The commit header should be up to 50 characters and the description up to 72 characters, [read more](https://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting).
- Branch style, [click](https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf#:~:text=own%20development%20cycle.-,Git%20Flow,-The%20Git%20Flow). It is suggested to use GitFlow. Don't forget to delete merged or close branches based on PR status. Development should be done in separate branches, it is not allowed to commit or merge changes directly into _master_ or _develop_.
- Commits, branches and PR's should contain small pieces of separate logic so that it can be revisited. For example, how to decompose and get started (documentation should also be updated):
  + The first PR would be enough to see poetry installed and a project structure.
  + The second PR can base interface and first version of scraper.
- Try to follow all [OOP](https://realpython.com/python3-object-oriented-programming/) & [design](https://www.boldare.com/blog/kiss-yagni-dry-principles/) principles.
- Submit the codebase along with a detailed README explaining how to set up and run the monolithic application, any additional features implemented, and any challenges faced. [Here is](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) a good cheat-list how to style documentation.
- Fork this repository and do your development there.


### Note:
- Use Python 3.10 or above.
- Feel free to use any additional libraries or tools you find suitable for the task.
- Try decomposing tasks into chunks and branches as described above.
- All `highlighted` words should be read in the documentation or familiarized with what they are.
- Follow best practices in terms of code readability, structure, and documentation.



### Suggested project structure:
```
./
├── src/
│   ├── core/
│   │   └── __init__.py
│   ├── selenium/
│   │   └── __init__.py
│   ├── b4s/
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
├── .env
├── .env.example
├── .gitignore
├── README.md
└── task.md
```
