from card.card import Card 

class DestinationCard(Card):
    def __init__(self, origin: str, destination: str, face_down : bool = True):
        super().__init__(card_type="Destination", value=(origin, destination), face_down = face_down)