import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card_package.card import Card


class DestinationCard(Card):
    def __init__(self, origin: str, destination: str, points: int):
        super().__init__(card_type="Destination", value=(origin, destination))
        if points <= 0:
            raise ValueError("destination cards must have positive values")
        self.points = points

    def get_number_of_points(self):
        return self.points

    def get_cities(self):
        return self.get_card_value()


if __name__ == "__main__":
    # create a destination card
    destination_card = DestinationCard("A", "B", 10)
    print(destination_card)
