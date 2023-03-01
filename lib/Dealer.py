import inquirer

from .Player import Player

BLACKJACK = 21


class Dealer(Player):
    def __init__(self, deck_cards: list) -> None:
        self.token_amount = 70
        self.name = "Dealer"
        # 1 card example: [{"symbol": "heart", "value": 1}]
        self.cards = []
        self.draw_card(deck_cards)

    def __repr__(self) -> str:
        return self.show_cards(True)

    def request_player_tokens(self, player: Player) -> int:
        bet_choices = [25, 50, 100]

        if bet_choices[0] > player.token_amount:
            return 0

        for i in range(1, len(bet_choices)):
            if bet_choices[i] > player.token_amount:
                bet_choices.pop(i)

        question = [
            inquirer.List(
                "bet",
                message=f"{player.name} how much do you want to bet?",
                choices=bet_choices,
            ),
        ]

        bet_answer = inquirer.prompt(question)

        if bet_answer is None:
            print("Not a valid answer!")
            exit()

        return bet_answer["bet"]

    def request_player_choice(self, player: Player, deck_cards: list) -> None:
        if player.total_cards_value() == BLACKJACK:
            return

        question = [
            inquirer.Confirm("hit", message="Do you want to hit?", default=False),
        ]

        answers = inquirer.prompt(question)

        if answers is None:
            print("Not a valid answer!")
            exit()

        hit = answers["hit"]

        if player.total_cards_value() == BLACKJACK:
            hit = False

        while hit:
            player.draw_card(deck_cards)
            print(player.show_cards(True))

            if player.total_cards_value() == BLACKJACK:
                break

            if player.total_cards_value() > BLACKJACK:
                break

            hit_answer = inquirer.prompt(
                [
                    inquirer.Confirm(
                        "hit", message="Do you want to hit?", default=False
                    ),
                ]
            )

            if hit_answer is None:
                print("Not a valid answer!")
                exit()

            hit = hit_answer["hit"]
