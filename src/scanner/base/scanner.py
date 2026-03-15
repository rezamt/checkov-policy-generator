from abc import ABC, abstractmethod


class Scanner(ABC):

    @abstractmethod
    def scan(self, url: str) -> list[str]:
        """Scan the given URL and return a list of results."""
        ...
