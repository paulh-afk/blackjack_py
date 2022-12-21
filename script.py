import yaml
import hashlib
import random


def name_to_symbol(name: str) -> str:
    return {
        'heart': card_symbols[0],
        'diamond': card_symbols[1],
        'spade': card_symbols[2],
        'club': card_symbols[3]
    }.get(name, 'Invalid symbol!')


def shuffle_deck(cards: list) -> list:
    index_list = [*range(len(cards))]
    shuffled_cards_deck = []

    while len(index_list):
        random_index = random.randrange(0, len(index_list))

        shuffled_cards_deck.append(cards[index_list[random_index]])
        index_list.pop(random_index)

    return shuffled_cards_deck


# Read "hash.txt"
try:
    with open('hash.txt', 'r') as file:
        check_sha1_hash = file.readline()
except FileNotFoundError:
    print('The file "hash.txt" does not exist')
    exit()

# Read and check "cards.yml" hash
try:
    with open('cards.yml', 'rb') as file:
        hasher = hashlib.sha1()

        while True:
            data = file.read()
            if not data:
                break
            hasher.update(data)

        if check_sha1_hash == hasher.hexdigest():
            print('"cards.yml" is authentic!')
            del hasher
        else:
            print('"cards.yml" is not authentic!')
            exit()

except FileNotFoundError:
    print('The file "cards.yml" does not exist')
    exit()

# Read and convert "cards.yml" to tuple
with open('cards.yml', 'r') as file:
    yaml_list = yaml.safe_load(file)
    cards = tuple(yaml_list)

    del yaml_list


card_symbols = ('♥', '♦', '♠', '♣')

deck_cards = shuffle_deck(cards)
dealer_cards = []
