# import argparse
from scrapper import Parser

# def parse_args():
#     parser = argparse.ArgumentParser(description='Portuguese words lookup.')
#     parser.add_argument('--definition', action='store_true', help='Lookup definition')
#     parser.add_argument('--synonym', action='store_true', help='Lookup synonym')
#     return parser.parse_args()


if __name__ == "__main__":
    # args = parse_args()
    p = Parser()
    while True:
        word_lookup = input('Lookup word -> ')
        if not word_lookup:
            break
        p.look_up(word_lookup)
        p.show()
