from deck.deck import Deck
from card.destination_card import DestinationCard
import json
from collections import deque

class DestinationCardDeck(Deck):
    def __init__(self):
        super().__init__()

        # Chargement des données depuis le fichier JSON
        with open("original_game_data\\1910.usa.tickets.json", "r") as fichier:
            donnees_json = json.load(fichier)
        self.cards = deque([DestinationCard(card["cities"][0], card["cities"][1], card["points"]) for card in donnees_json])
        