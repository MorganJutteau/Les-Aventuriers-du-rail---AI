from abc import ABC, abstractmethod
from deck.destination_card_deck import DestinationCardDeck
from deck.transport_card_deck import TransportCardDeck

class Player(ABC):
    def __init__(self, transport_cards : TransportCardDeck, destination_cards : DestinationCardDeck):
        self.transport_cards = [transport_cards.draw() for i in range(4)]
        self.destination_cards = self.choose_destination_cards(self, destination_cards, in_game=False)
        self.score = 0
        
    @abstractmethod
    def get_action(self, player_input):
        pass

    @abstractmethod
    def choose_destination_cards(self, destination_cards, in_game : bool):
        """
        If in_game is set to True a player has to keep at least 1 of the 3 drawn destination cards.
        If in_game is set to False a player has to keep at least 2 of the 3 drawn destination cards.
        """
        pass
