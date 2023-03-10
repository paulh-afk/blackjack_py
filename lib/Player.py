from .cards import (
    name_to_symbol,
    is_honor_card,
    honor_card_name_to_fullname,
    honor_card_name_to_value,
)
from terminaltables import AsciiTable

BLACKJACK = 21


class Player:
    def __init__(self, name: str, deck_cards: list) -> None:
        self.token_amount = 70
        self.name = name
        # 1 card example: [{"symbol": "heart", "value": 1}]
        self.cards = []
        for _ in range(2):
            self.draw_card(deck_cards)

    def __repr__(self) -> str:
        return self.name + " has " + str(self.token_amount) + " tokens"

    def draw_card(self, deck_cards: list) -> None:
        self.cards.append(deck_cards[-1])
        deck_cards.pop()

    def show_cards(self, show_player_name: bool = False) -> str:
        table_data = [["Symbol", "Value"]]

        for card in self.cards:
            card_value = card["value"]
            honor_value_name = None

            if is_honor_card(card_value):
                honor_value_name = honor_card_name_to_fullname(card_value)
                card_value = honor_card_name_to_value(card_value)

                if type(card_value) is tuple:
                    card_value_list = [str(value) for value in card_value]
                    card_value = "/".join(card_value_list)

            row = [
                name_to_symbol(card["symbol"])
                + " ({symbol_name})".format(symbol_name=card["symbol"])
            ]

            if honor_value_name is None:
                row.append(card_value)
            else:
                row.append(honor_value_name + " ({value})".format(value=card_value))

            table_data.append(row)

        total_cards_value_str = str(self.total_cards_value())
        total_row = ["Total", total_cards_value_str]
        table_data.append(total_row)

        title = None

        if show_player_name:
            title = self.name

        return AsciiTable(table_data, title).table

    def total_cards_value(self) -> int:
        total = 0

        cards_honor_cards_value = [
            honor_card_name_to_value(card["value"])
            if is_honor_card(card["value"])
            else card["value"]
            for card in self.cards
        ]

        # The last card is an ace to determine its value
        for i in range(len(cards_honor_cards_value)):
            if (type(cards_honor_cards_value[i]) is tuple) and (
                i + 1 != len(cards_honor_cards_value)
            ):
                card = cards_honor_cards_value[i]
                cards_honor_cards_value.pop(i)
                cards_honor_cards_value.append(card)

        for card_value in cards_honor_cards_value:
            if type(card_value) is tuple:
                if total <= (BLACKJACK - card_value[1]):
                    total += card_value[1]
                else:
                    total += card_value[0]
            else:
                total += card_value

        return total
