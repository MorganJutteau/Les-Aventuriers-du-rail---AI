from deck.deck import Deck
from deck.destination_card_deck import DestinationCardDeck
from deck.transport_card_deck import TransportCardDeck
from card.card import Card
from card.destination_card import DestinationCard
from card.transport_card import TransportCard

# Instanciation des decks
destination_deck = DestinationCardDeck()
transport_deck = TransportCardDeck()

# Affichage de quelques cartes pour vérifier
for _ in range(5):
    destination_card = destination_deck.draw()
    print(f"Destination Card: {destination_card}")

for _ in range(5):
    transport_card = transport_deck.draw()
    print(f"Transport Card: {transport_card}")