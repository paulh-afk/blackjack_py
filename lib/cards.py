import random

card_symbols = ("♥", "♦", "♠", "♣")
honor_cards = ("A", "J", "Q", "K")


def name_to_symbol(name: str) -> str:
    return {
        "heart": card_symbols[0],
        "diamond": card_symbols[1],
        "spade": card_symbols[2],
        "club": card_symbols[3],
    }.get(name, "Invalid symbol!")


def is_honor_card(card_value: str) -> bool:
    return bool(honor_cards.count(card_value))


def honor_card_name_to_value(card_value: str) -> tuple | int:
    if card_value == "A":
        return (1, 11)
    else:
        return 10


def honor_card_name_to_fullname(card: str) -> str:
    return {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}.get(card)


def shuffle_deck(cards: list) -> list:
    index_list = list(range(len(cards)))
    shuffled_cards_deck = []

    while len(index_list):
        random_index = random.randrange(0, len(index_list))

        shuffled_cards_deck.append(cards[index_list[random_index]])
        index_list.pop(random_index)

    return shuffled_cards_deck
