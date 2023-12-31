from card.card import Card

class TransportCard(Card):
    def __init__(self, color: str):
        super().__init__(card_type="Transport", value=color)