from .Player import Player


class Dealer(Player):
    def __init__(self, deck_cards: list) -> None:
        super().__init__("Dealer", deck_cards)

    def __repr__(self) -> str:
        return self.show_cards(True)
