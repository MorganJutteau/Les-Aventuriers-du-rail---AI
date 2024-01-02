import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deck_package.destination_card_deck import DestinationCardDeck
from deck_package.transport_card_deck import TransportCardDeck
from player_package.player import Player
from player_package.player_action import *


class HumanPlayer(Player):
    def get_action(self):
        self.print_status()
        # get the action from the player

        print("What would you like to do?")
        print(
            f"1. Draw a transport card : {DRAW_TRANSPORT} <indice_1> <indice_2> or {DRAW_TRANSPORT} <index> (indices are from 0, use 5 for drawing from downside cards))"
        )
        print(f"2. Draw a destination card : {DRAW_DESTINATION}")
        print(f"3. Build on a link : {BUILD} <node_a> <node_b>")

        while True:
            action = input("Enter your action: ")
            action = action.split(" ")
            action_type = action[0]
            args = action[1:]

            try:
                return PlayerAction(action_type, args)
            except ValueError as e:
                print(e)

    def print_status(self):
        # print the board
        print(self.game_status.board)

        # print the player's hand
        print("Your hand:")
        print(self.game_status.player_transport_cards[self.game_status.current_player])

        # print the player's destination cards
        print("Your destination cards:")
        print(
            self.game_status.players_destination_cards[self.game_status.current_player]
        )

        # print the player's points
        print("Your points:")
        print(
            self.game_status.point_counter.get_points(self.game_status.current_player)
        )

        # print the visible transport cards
        print("Visible transport cards:")
        print(self.game_status.transport_deck.upside_cards)

    def choose_destination_cards(self, destination_card_pool, in_game: bool):
        print("Choose your destination cards:")
        print(destination_card_pool)

        if in_game:
            print("You have to keep at least 1 of these cards")
        else:
            print("You have to keep at least 2 of these cards")

        while True:
            indices = input(
                "Enter the indices of the cards you want to keep (starts from 0): "
            )
            indices = indices.split(" ")
            indices = [int(i) for i in indices]

            if len(indices) < 1:
                print("You have to keep at least 1 card")
                continue

            if len(indices) > 2 and in_game:
                print("You can only keep 1 card")
                continue

            if len(indices) > 3 and not in_game:
                print("You can only keep 2 cards")
                continue

            try:
                return indices
            except IndexError:
                print("Invalid index")
