from card_package.card import Card


class TransportCard(Card):
    # string constants for colors
    WHITE = "blanc"
    BLUE = "bleu"
    YELLOW = "jaune"
    ORANGE = "orange"
    BLACK = "noir"
    RED = "rouge"
    GREEN = "vert"
    PURPLE = "violet"
    LOCOMOTIVE = "locomotive"

    def __init__(self, color: str):
        super().__init__(card_type="Transport", value=color)

    def get_color(self):
        return self.get_card_value()
