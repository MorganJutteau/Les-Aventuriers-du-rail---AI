from deck.destination_card_deck import DestinationCardDeck
from deck.transport_card_deck import TransportCardDeck
from player.player import Player

class HumanPlayer(Player):
    def __init__(self, transport_cards: TransportCardDeck, destination_cards: DestinationCardDeck):
        super().__init__(transport_cards, destination_cards)
