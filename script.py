import yaml
import hashlib

from lib.utils import user_input, user_input_int

import lib.cards as cards_lib
from lib.Player import Player
from lib.Dealer import Dealer

BLACKJACK = 21


def init_players_hands() -> list:
    players_number = user_input_int("How many players are ready to play? (1-5) ")

    if players_number < 1 or players_number > 5:
        print("Invalid value, the number of players must be between 1 and 5!")
        exit()

    players = []

    for i in range(1, players_number + 1):
        player_name = user_input(f"Player {i} enter your name: ")
        players.append(Player(player_name, deck_cards))

    return players


# Read "hash.txt"
try:
    with open("hash.txt", "r") as file:
        check_sha1_hash = file.readline()

except FileNotFoundError:
    print('The file "hash.txt" does not exist')
    exit()

# Read and check "cards.yml" hash
try:
    with open("cards.yml", "rb") as file:
        hasher = hashlib.sha1()

        while True:
            data = file.read()
            if not data:
                break
            hasher.update(data)

        if check_sha1_hash != hasher.hexdigest():
            print('"cards.yml" is not authentic!')
            exit()

        del hasher, check_sha1_hash

except FileNotFoundError:
    print('The file "cards.yml" does not exist')
    exit()

# Read and convert "cards.yml" to tuple
with open("cards.yml", "r") as file:
    yaml_list = yaml.safe_load(file)
    cards = tuple(yaml_list)

    del yaml_list


deck_cards = cards_lib.shuffle_deck(cards)

players = init_players_hands()
dealer = Dealer(deck_cards)

players_token_bet = [0 for _ in players]

for i in range(len(players)):
    player = players[i]

    token_bet = dealer.request_player_tokens(player)
    if token_bet == 0:
        print(player.name + " does not have enough tokens to participate")
        continue

    print(dealer)

    print(player.show_cards(True))

    players_token_bet[i] = token_bet

    dealer.request_player_choice(player, deck_cards)

    player_cards_value = player.total_cards_value()

    if player_cards_value == BLACKJACK:
        print(player.name + " does BLACKJACK!")
    elif player_cards_value > BLACKJACK:
        print(f"Total value of {player.name} cards exceeds 21")


print(dealer)

while dealer.total_cards_value() < 17:
    dealer.draw_card(deck_cards)
    print(dealer)

if dealer.total_cards_value() > BLACKJACK:
    print(dealer.name + f" exceeds BLACKJACK ({str(BLACKJACK)})")


for i in range(len(players)):
    player = players[i]

    player_cards_value = player.total_cards_value()
    dealer_cards_value = dealer.total_cards_value()

    if player_cards_value < dealer_cards_value or player_cards_value > BLACKJACK:
        player.token_amount -= players_token_bet[i]

    elif (
        player_cards_value < BLACKJACK and player_cards_value != dealer_cards_value
    ) or (player_cards_value == BLACKJACK and dealer_cards_value != BLACKJACK):
        player.token_amount += players_token_bet[i]


for player in players:
    print(player)

print(dealer)
