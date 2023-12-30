from card.card import Card
from random import shuffle
from typing import Deque

class Deck:
    def __init__(self):
        self.cards : Deque[Card] = Deque([])
    def shuffle(self):
        shuffle(self.cards)
    def draw(self):
        return self.cards.popleft()
    def add_card(self, card : Card):
        self.cards.append(card)
        