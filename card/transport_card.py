from card.card import Card

class TransportCard(Card):
    def __init__(self, color: str, face_down: bool = True):
        super().__init__(card_type="Transport", value=color, face_down = face_down)