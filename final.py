
import logging

logger = logging.getLogger(__file__)

class WordNumberLookUp:
    """A class that provides a word that is associated with a number."""

    def __init__(self, initial: dict[int, str]=dict()):
        """Initializes the WordNumberLookUp class with an initial lookup dictionary if provided."""
        self._lookup = initial if initial is not None else dict()
    
    def add_word(self, num_key: int, word: str):
        """Adds an entry to the lookup."""
        logger.info("Adding word '%s' to lookup with key '%d'", word, num_key)
        self._lookup[num_key] = word
    
    def get_word_by_number(self, num_key: int) -> str | None:
        """Returns the word from its lookup number"""
        try:
            return self._lookup[num_key]
        except KeyError as e:
            logger.exception("The key '%d' was not in the lookup", num_key, exc_info=e)
            return None

if __name__ == "__main__":
    # Set up logging configuration
    logging.basicConfig(level=logging.DEBUG)

    lookup = WordNumberLookUp({1: "one", 2: "two"})
    lookup.add_word(3, "three")

    word = lookup.get_word_by_number(2)
    print(f"The word associated with 2 is '{word}'")
