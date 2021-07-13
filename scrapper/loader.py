from typing import Dict
import re

import requests
from bs4 import BeautifulSoup


class Loader:
    """
    Sends a requests to dicio.com.br
    and parses it with BeautifulSoup
    """
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }
    BASE_URL = 'https://www.dicio.com.br'

    def __init__(self):
        pass

    def request(self, word_lookup: str) -> Dict:
        """
        Scrapes and returns information such as definition of a given word

        :param word_lookup: Word to look up in portuguese dictionary
        :return: dict containing bs4 Tags for synonyms, definition, etc
        """
        if not word_lookup:
            return None
        url = f'{self.BASE_URL}/{word_lookup}'
        request = requests.get(url, headers=self.HEADER)
        if request.status_code == 404:
            print('Palabra no encontrada!')
            return None
        soup = BeautifulSoup(request.text, 'html.parser')
        # synonyms, definition = soup.find_all('p', class_='adicional', limit=2)
        definition = soup.find('h2', text=re.compile('Definição de'))
        if definition is not None:
            definition = definition.parent.p
        synonyms = soup.find('h2', text=re.compile('Sinônimos de'))
        if synonyms is not None:
            synonyms = synonyms.parent.p
        out = {
            'synonyms': synonyms,
            'definition': definition
        }
        return out
