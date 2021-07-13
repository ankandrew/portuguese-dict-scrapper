from typing import List

from .loader import Loader


class Parser:
    """
    Parse and clean given bs4 tags
    """

    def __init__(self, word_lookup: str) -> None:
        self.loader = Loader()
        self.load_result = self.loader.request(word_lookup)

    def look_up(self, word_lookup: str) -> None:
        """
        Look up another word
        """
        self.load_result = self.loader.request(word_lookup)

    def get_synonyms(self) -> List:
        synonyms = self.load_result.get('synonyms')
        return [a.text for a in synonyms.find_all('a')]

    def get_definition(self) -> List:
        definition = self.load_result.get('definition')
        return [text.strip() for text in definition.text.strip().split('\n')]

    def show(self) -> None:
        """
        Print all extracted features in a nice way
        """
        print('Synonyms: ', end='\n\n')
        synonyms = self.get_synonyms()
        for i, synonym in enumerate(synonyms):
            msg = f'{synonym}, ' if i < len(synonyms) - 1 else f'{synonym}\n\n'
            print(msg, end='')
        definition = self.get_definition()
        for d in definition:
            print(d)

    # # REMOVE
    # @staticmethod
    # def clean_str(s: str) -> str:
    #     return s.strip().replace('\n', '')
