import uuid
from dataclasses import dataclass
from typing import NoReturn
import requests

@dataclass
class ApiService:
    def __init__(self, hostname: str) -> None:
        """
        Constructs a new BankingService object with the given hostname.

        Args:
            hostname: The hostname of the banking API service.
        """
        self.hostname: str = hostname

    def call(self):
        try:    
            print("HERE")
            url = "http://127.0.0.1:5000/"
          # url ="https://dummy-json.mock.beeceptor.com/continents"
                       #params = {"page": 1, "per_page": 20}   # query parameters

            response = requests.get(url, timeout=5)
            response.raise_for_status()             # raise exception on HTTP error

            data = response.json()                  # parse JSON body

            result = f"Transfer complete (transaction IDs: {data})"
            return result

        except Exception:
            raise 