cards = (
    {
        'symbol': 'heart',
        'value': 1
    },
    {
        'symbol': 'diamond',
        'value': 1
    },
    {
        'symbol': 'spade',
        'value': 1
    },
    {
        'symbol': 'club',
        'value': 1
    },
)

symbols = ('♥', '♦', '♠', '♣')

game_cards = []
dealer_cards = []


def name_to_symbol(name):
    return {
        'heart': symbols[0],
        'diamond': symbols[1],
        'spade': symbols[2],
        'club': symbols[3]
    }.get(name, 'Invalid symbol!')

