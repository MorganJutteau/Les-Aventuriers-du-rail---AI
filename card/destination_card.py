from card.card import Card 

class DestinationCard(Card):
    def __init__(self, origin: str, destination: str, points : int):
        super().__init__(card_type="Destination", value=(origin, destination))
        if points<=0:
            raise ValueError("destination cards must have positive values")
        self.points = points
    
    def get_number_of_points(self):
        return self.points