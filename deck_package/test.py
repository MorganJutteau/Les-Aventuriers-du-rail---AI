import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deck_package.deck import Deck
from deck_package.destination_card_deck import DestinationCardDeck
from deck_package.transport_card_deck import TransportCardDeck
from card_package.card import Card
from card_package.destination_card import DestinationCard
from card_package.transport_card import TransportCard

# Deck instanciation
destination_deck = DestinationCardDeck()
transport_deck = TransportCardDeck()

# Printing a few cards from each deck
for _ in range(5):
    destination_card = destination_deck.draw()
    print(f"Destination Card: {destination_card}")

for _ in range(5):
    transport_card = transport_deck.draw()
    print(f"Transport Card: {transport_card}")
