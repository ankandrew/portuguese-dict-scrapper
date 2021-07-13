## Portuguese dictionary scrapper

Convenience tool for scrapping features of a given portuguese word.
Source of information is [dicio](https://www.dicio.com.br/).

### Installation

`pip install -r requirements.txt`

### Usage

```python
from scrapper import Parser

p = Parser('coco')

# Get synonyms as list
synonyms = p.get_synonyms()

# Get definition as list
definition = p.get_definition()

# Show synonyms & definition
p.show()

# Change word
p.look_up('casa')
# Show new word definition & synonyms
p.show()
```

#### Output for 'coco'
```
Synonyms: 

cabeça, embolada, cabaça, coqueiro

Classe gramatical: adjetivo de dois gêneros e substantivo de dois gêneros
Flexão do verbo cocar na: 1ª pessoa do singular do presente do indicativo
Separação silábica: co-co
Plural: cocos
```

### TODO

- [x] Synonyms
- [ ] Fine-grain definition (i.e. gender)
- [ ] Scrape examples
- [ ] Scrape sentences
- [ ] Interactive args
