from deck.deck import Deck
from card.destination_card import DestinationCard
import json
from collections import deque

class DestinationCardDeck(Deck):
    def __init__(self):
        super().__init__()

        # data is loaded from a json file
        with open("original_game_data\\1910.usa.tickets.json", "r") as file:
            json_data = json.load(file)
        self.cards = deque([DestinationCard(card["cities"][0], card["cities"][1], card["points"]) for card in json_data])

        # the deck is then shuffled
        self.shuffle()