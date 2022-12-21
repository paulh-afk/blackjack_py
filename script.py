import yaml
import hashlib

# Read hash.txt
try:
    with open('hash.txt', 'r') as file:
        check_sha1_hash = file.readline()
except FileNotFoundError:
    print('The file "hash.txt" does not exist')
    exit()

# Read and check cards.yml hash
try:
    with open('cards.yml', 'rb') as file:
        hasher = hashlib.sha1()

        while True:
            data = file.read()
            if not data:
                break
            hasher.update(data)

        print(check_sha1_hash)
        print(hasher.hexdigest())

        if check_sha1_hash == hasher.hexdigest():
            print('Valid file!')
        else:
            print('Invalid file')
            exit()

except FileNotFoundError:
    print('The file "cards.yml" does not exist')
    exit()

card_symbols = ('♥', '♦', '♠', '♣')

game_cards = []
dealer_cards = []


def name_to_symbol(name):
    return {
        'heart': card_symbols[0],
        'diamond': card_symbols[1],
        'spade': card_symbols[2],
        'club': card_symbols[3]
    }.get(name, 'Invalid symbol!')
