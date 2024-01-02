import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_status_package.point_counter import PointCounter
from deck_package.transport_card_deck import TransportCardDeck
from deck_package.destination_card_deck import DestinationCardDeck
from card_package.transport_card import TransportCard


class PlayerHand:
    def __init__(self):
        self.transport_cards = {
            TransportCard.WHITE: 0,
            TransportCard.BLUE: 0,
            TransportCard.YELLOW: 0,
            TransportCard.ORANGE: 0,
            TransportCard.BLACK: 0,
            TransportCard.RED: 0,
            TransportCard.GREEN: 0,
            TransportCard.PURPLE: 0,
            TransportCard.LOCOMOTIVE: 0,
        }
        self.destination_cards = []

    def add_transport_card(self, card):
        self.transport_cards[card.get_color()] += 1

    def add_destination_card(self, card):
        self.destination_cards.append(card)

    def remove_transport_cards(self, color, amount):
        self.transport_cards[color] -= amount

    def get_number_of_transport_cards(self, color):
        return self.transport_cards[color]

    def __str__(self) -> str:
        return f"Transport cards: {self.transport_cards}\nDestination cards: {self.destination_cards}"

    def __repr__(self) -> str:
        return str(self)


class GameStatus:
    def __init__(self, init_board, number_of_players):
        self.board = init_board

        # TODO: initialize these
        self.transport_deck = TransportCardDeck()
        self.destination_deck = DestinationCardDeck()

        self.player_hands = [PlayerHand() for _ in range(number_of_players)]

        for i in range(number_of_players):
            for _ in range(4):
                self.player_hands[i].add_transport_card(self.transport_deck.draw())

        self.players_wagons_left = [45 for _ in range(number_of_players)]

        self.current_player = 0
        self.point_counter = PointCounter(number_of_players)

        self.final_turn_trigger_player = None
        self.game_over = False

        self.shown_destination_cards = []

        self.current_turn = -number_of_players

        self.number_of_players = number_of_players

    def build_on_link(self, node_a, node_b):
        assert self.check_build_legality(node_a, node_b)
        self.board.build_on_link(node_a, node_b, self.current_player)
        self.point_counter.on_build(self.current_player, node_a, node_b, self.board)

        link = self.board.get_link(node_a, node_b)
        required_color_count = self.player_hands[
            self.current_player
        ].get_number_of_transport_cards(link.color)

        if required_color_count >= link.length:
            # remove the required transport cards from the player's hand
            self.player_hands[self.current_player].remove_transport_cards(
                link.color, link.length
            )

        else:
            # remove all cards of the color
            self.player_hands[self.current_player].remove_transport_cards(
                link.color, required_color_count
            )

            # complete with locomotives
            locomotive_count = self.player_hands[
                self.current_player
            ].get_number_of_transport_cards(TransportCard.LOCOMOTIVE)

            self.player_hands[self.current_player].remove_transport_cards(
                TransportCard.LOCOMOTIVE, link.length - required_color_count
            )

        # remove the wagons from the player's wagons left
        self.players_wagons_left[self.current_player] -= link.length

    def draw_transport_cards(self, indices_list):
        # 5: draw from downside cards
        # i: draw from upside cards at index i

        assert self.check_transport_card_drawing_legality(indices_list)

        for index in indices_list:
            if index == 5:
                # draw from downside cards
                self.player_hands[self.current_player].add_transport_card(
                    self.transport_deck.draw_downside_card()
                )
            else:
                # draw from upside cards
                self.player_hands[self.current_player].add_transport_card(
                    self.transport_deck.draw_upside_card(index)
                )

    def draw_destination_cards_phase_1(self):
        # draw 3 destination cards
        # return the 3 destination cards
        self.shown_destination_cards = [self.destination_deck.draw() for _ in range(3)]
        return self.shown_destination_cards

    def draw_destination_cards_phase_2(self, chosen_dc_indices):
        # choose 2 destination cards
        # return the indices of the 2 destination cards

        assert self.check_destination_card_drawing_legality(chosen_dc_indices)

        # add chosen destination cards to player's destination cards
        for index in chosen_dc_indices:
            self.player_hands[self.current_player].add_destination_card(
                self.shown_destination_cards[index]
            )

        self.shown_destination_cards = []

        return chosen_dc_indices

    def check_destination_card_drawing_legality(self, chosen_dc_indices):
        # in pre_game, the player must draw at least 2 destination cards
        # in game, the player must draw at least 1 destination card

        pre_game = self.current_turn < 0
        if pre_game:
            if len(chosen_dc_indices) < 2:
                return False
        else:
            if len(chosen_dc_indices) < 1:
                return False

        return True

    def check_transport_card_drawing_legality(self, indices_list):
        # the player must draw at least 1 transport card
        if len(indices_list) < 1:
            return False

        # the player must not draw more than 2 transport cards
        if len(indices_list) > 2:
            return False

        # the player must not draw more than 1 locomotive
        nbLocomotives = 0
        for index in indices_list:
            if index == 5:
                nbLocomotives += 1
        if nbLocomotives > 1:
            return False

        return True

    def check_build_legality(self, node_a, node_b):
        # the link must not be already built on
        link = self.board.get_link(node_a, node_b)
        if link.occupied:
            return False

        # the player must have the required transport cards
        required_color_count = self.player_hands[
            self.current_player
        ].get_number_of_transport_cards(link.color)
        locomotive_count = self.player_hands[
            self.current_player
        ].get_number_of_transport_cards(TransportCard.LOCOMOTIVE)

        if required_color_count + locomotive_count < link.length:
            return False

        # the player must have enough wagons left
        if self.players_wagons_left[self.current_player] < link.length:
            return False

        return True

    def end_turn(self):
        # If the player has 2 wagons or less left, the game will end after his next turn
        if self.final_turn_trigger_player is None:
            if self.players_wagons_left[self.current_player] <= 2:
                self.final_turn_trigger_player = self.current_player
        else:
            if self.current_player == self.final_turn_trigger_player:
                self.game_over = True

        self.current_player = (self.current_player + 1) % self.number_of_players
        self.current_turn += 1

    # Getters (used by players)
    def get_player_hand(self):
        return self.players_hands[self.current_player]

    def get_player_points(self, player):
        return self.point_counter.get_points(player)

    def get_board(self):
        return self.board

    def draw_three_destination_cards(self):
        return [self.destination_deck.draw() for _ in range(3)]
