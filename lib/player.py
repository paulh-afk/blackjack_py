from .cards import (
    distribute_cards,
    name_to_symbol,
    is_honor_card,
    honor_card_name_to_fullname,
    honor_card_name_to_value,
)
from terminaltables import AsciiTable


class Player:
    name = ""
    token_amount = 500
    cards = []

    def __init__(self, name: str, deck_cards: list) -> None:
        self.name = name
        self.cards = distribute_cards(deck_cards)

    def __repr__(self) -> str:
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

        table = AsciiTable(table_data, self.name)

        return (
            self.name
            + " has "
            + str(self.token_amount)
            + " tokens and holds the cards:\n"
            + table.table
        )
