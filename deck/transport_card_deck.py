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

        # getting 5 face up cards
        self.upside_cards = [self.cards.popleft() for i in range(5)]
    
    def get_upside_cards(self):
        return self.upside_cards
    
    def draw_upside_card(self, position : int):
        """
        position represents the card position in the upside_card list. 0 = first, 4 = last
        """
        card = self.upside_cards.pop(position)
        self.upside_cards[position] = self.draw()

        return card