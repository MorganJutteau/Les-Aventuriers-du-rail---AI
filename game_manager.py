import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_status_package.game_status import GameStatus


class GameManager:
    def __init__(self, players, init_board):
        # create game status
        self.game_status = GameStatus(init_board, len(players))
        self.players = players
        for player in players:
            player.set_game_status(self.game_status)
        self.choose_initial_destination_cards()

    def choose_initial_destination_cards(self):
        for i, player in enumerate(self.players):
            # draw 3 destination cards
            destination_card_pool = [
                self.game_status.destination_deck.draw() for _ in range(3)
            ]
            # choose 2 destination cards
            chosen_dc_index = player.choose_destination_cards(
                destination_card_pool, in_game=False
            )
            # add chosen destination cards to player's destination cards
            self.game_status.players_destination_cards[i] = [
                destination_card_pool[index] for index in chosen_dc_index
            ]

    def run(self):
        # TODO: implement
        pass
