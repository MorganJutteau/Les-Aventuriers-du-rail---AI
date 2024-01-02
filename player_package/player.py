import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod
from deck_package.destination_card_deck import DestinationCardDeck
from deck_package.transport_card_deck import TransportCardDeck


class Player(ABC):
    def set_game_status(self, game_status):
        self.game_status = game_status

    @abstractmethod
    def get_action(self):  # -> PlayerAction
        pass

    @abstractmethod
    def choose_destination_cards(
        self, destination_card_pool, in_game: bool
    ):  # -> List[DestinationCard]
        """
        If in_game is set to True a player has to keep at least 1 of the 3 drawn destination cards.
        If in_game is set to False a player has to keep at least 2 of the 3 drawn destination cards.
        """
        pass
