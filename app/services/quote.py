import json
import os
import random
from typing import Any, Dict, List

from app.conf import settings


class QuoteService:
    FILE_NAME = "data/quotes.json"

    def __init__(self) -> None:
        """
        It creates a class called QuoteModel.
        """
        self.quotes: List[Dict[str, Any]] = []

    def load(self):
        """
        It opens the file, reads the contents, and then loads the contents
        into the quotes variable.
        """
        with (
            open(
                os.path.join(
                    settings.BASE_DIR,
                    self.FILE_NAME,
                ),
                "r",
            ) as quotes_file
        ):
            self.quotes = json.loads(quotes_file.read())

    def get_quote(self) -> Dict[str, Any]:
        """
        Return a random quote from the list of quotes.
        :return: A dictionary with a key of "quote" and a value of a random
        quote from the quotes list.
        """
        return self.quotes[random.randint(0, len(self.quotes) - 1)]
