from typing import Any, Protocol


class WebScraperInterface(Protocol):
    def initialize_scraper(self) -> None:
        ...

    def navigate_to_page(self, url: str) -> None:
        ...

    def extract_data(self) -> Any:
        ...

    def write_data(self, data: Any, filename: str) -> None:
        ...

    def apply_filters(self, **kwargs) -> None:
        ...
