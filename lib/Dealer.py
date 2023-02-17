import inquirer

from .Player import Player

BLACKJACK = 21


class Dealer(Player):
    def __init__(self, deck_cards: list) -> None:
        super().__init__("Dealer", deck_cards)

    def __repr__(self) -> str:
        return self.show_cards(True)

    def request_player_choice(self, player: Player, deck_cards: list):
        questions = [
            inquirer.List(
                "bet", message="How much do you want to bet?", choices=[25, 50, 100]
            ),
            inquirer.Confirm("hit", message="Do you want to hit?", default=False),
        ]

        answers = inquirer.prompt(questions)

        if answers is None:
            print("Not a valid answer!")
            exit()

        hit = answers["hit"]

        if player.total_cards_value() == BLACKJACK:
            print("BLACKJACK!")
            hit = False

        while hit:
            player.draw_card(deck_cards)
            print(player.show_cards(True))

            if player.total_cards_value() == BLACKJACK:
                print("BLACKJACK!")
                hit = False

            if player.total_cards_value() > BLACKJACK:
                print(
                    player.name
                    + " the total value of the cards is above "
                    + str(BLACKJACK)
                    + ", you lose "
                    + str(answers["bet"])
                    + " tokens!"
                )
                player.token_amount -= answers["bet"]
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
