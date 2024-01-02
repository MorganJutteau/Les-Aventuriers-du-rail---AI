import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_status_package.point_counter import PointCounter
from deck_package.transport_card_deck import TransportCardDeck
from deck_package.destination_card_deck import DestinationCardDeck


class GameStatus:
    def __init__(self, init_board, number_of_players):
        self.board = init_board

        # TODO: initialize these
        self.transport_deck = TransportCardDeck()
        self.destination_deck = DestinationCardDeck()
        self.player_transport_cards = [
            [self.transport_deck.draw() for i in range(4)]
            for _ in range(number_of_players)
        ]

        # will be populated in choose_initial_destination_cards by the game manager
        self.players_destination_cards = [[] for _ in range(number_of_players)]

        self.current_player = 0
        self.point_counter = PointCounter(number_of_players)

    def build_on_link(self, node_a, node_b):
        # TODO : implement legality check and update player hand
        self.board.build_on_link(node_a, node_b, self.current_player)
        self.point_counter.on_build(self.current_player, node_a, node_b, self.board)

    def draw_transport_cards(self, indices_list):
        # TODO : implement
        # 5: draw from downside cards
        # i: draw from upside cards at index i
        # check that the indices_list is at most 2 elements long

        if len(indices_list) > 2:
            raise ValueError("Too many cards drawn")

        # check that no two locomotives are drawn from upside cards
        upside_cards = self.transport_deck.get_upside_cards()
        nbLocomotives = 0
        for index in indices_list:
            if index != 5:
                if self.transport_deck.upside_cards[index].get_color() == "locomotive":
                    nbLocomotives += 1
        if nbLocomotives > 1:
            raise ValueError("Too many locomotives drawn from upside cards")

        for index in indices_list:
            if index == 5:
                # draw from downside cards
                self.player_transport_cards[self.current_player].append(
                    self.transport_deck.draw()
                )
            else:
                self.player_transport_cards[self.current_player].append(
                    self.transport_deck.draw_upside_card(index)
                )

    def draw_destination_card(self):
        # TODO : implement
        pass

    def end_turn(self):
        self.current_player = (self.current_player + 1) % len(self.player_data)

    # Getters (used by players)
    def get_player_hand(self):
        return self.players_hands[self.current_player]

    def get_player_destination_cards(self):
        return self.players_destination_cards[self.current_player]

    def get_player_points(self, player):
        return self.point_counter.get_points(player)

    def get_board(self):
        return self.board

    def draw_three_destination_cards(self):
        return [self.destination_deck.draw() for _ in range(3)]
