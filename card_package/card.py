class Card:
    def __init__(self, card_type: str, value):
        self.card_type = card_type
        self.value = value

    def __str__(self) -> str:
        return f"{self.card_type} - {self.value}"

    def __repr__(self) -> str:
        return f"{self.card_type} - {self.value}"

    def get_card_type(self):
        return self.card_type

    def get_card_value(self):
        return self.value
