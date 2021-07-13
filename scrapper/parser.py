from typing import List

from .loader import Loader


class Parser:
    """
    Parse and clean given bs4 tags
    """

    def __init__(self, word_lookup: str = None) -> None:
        self.loader = Loader()
        self.load_result = self.loader.request(word_lookup)

    def look_up(self, word_lookup: str) -> None:
        """
        Look up another word
        """
        self.load_result = self.loader.request(word_lookup)

    def get_synonyms(self) -> List:
        synonyms = self.load_result.get('synonyms')
        if synonyms is not None:
            synonyms = [a.text for a in synonyms.find_all('a')]
        else:
            synonyms = ['N/A']
        return synonyms

    def get_definition(self) -> List:
        definition = self.load_result.get('definition')
        if definition is not None:
            definition = [text.strip() for text in definition.text.strip().split('\n')]
        else:
            definition = ['N/A']
        return definition

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
