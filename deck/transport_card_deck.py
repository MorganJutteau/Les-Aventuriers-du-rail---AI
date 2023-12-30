from deck.deck import Deck
from card.transport_card import TransportCard

class TransportCardDeck(Deck):
    def __init__(self):
        super().__init__()

        # chargement des cartes transport classique
        for i in range(12):
            self.add_card(TransportCard(color = "blanc"))
            self.add_card(TransportCard(color = "bleu"))
            self.add_card(TransportCard(color = "jaune"))
            self.add_card(TransportCard(color = "vert"))
            self.add_card(TransportCard(color = "rouge"))
            self.add_card(TransportCard(color = "violet"))
            self.add_card(TransportCard(color = "noir"))
            self.add_card(TransportCard(color = "orange"))
        
        # chargement des cartes locomotive
        for i in range(14):
            self.add_card(TransportCard(color = "locomotive"))
        
        # mélange des cartes
        self.shuffle()