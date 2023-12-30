from deck.deck import Deck
from card.transport_card import TransportCard
import json
from collections import deque

class TransportCardDeck(Deck):
    def __init__(self):
        super().__init__()

        # data is loaded from a json file
        with open("original_game_data\\color_cards.json", "r") as file:
            json_data = json.load(file)
        self.cards = deque([TransportCard(color = card["color"]) for card in json_data])
        
        # the deck is then shuffled
        self.shuffle()