from .cards import distribute_cards


class Player:
    name = ''
    token_amount = 500
    cards = []

    def __init__(self, name: str, deck_cards: list) -> None:
        self.cards = distribute_cards(deck_cards)

    def __str__(self) -> str:
        return self.name + ' has ' + self.token_amount + ' tokens '
