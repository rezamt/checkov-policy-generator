import requests
from bs4 import BeautifulSoup
from src.scanner.base.scanner import Scanner


class AWSManagedPolicyScanner(Scanner):

    def scan(self, url: str) -> list[str]:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        main = soup.find("div", id="main-col-body")
        if not main:
            return []

        return [a.text.strip() for a in main.select("div.highlights ul li p a")]
