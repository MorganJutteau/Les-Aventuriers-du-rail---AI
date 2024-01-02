import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_status_package.game_status import GameStatus
from player_package.player_action import PlayerAction


class GameManager:
    def __init__(self, players, init_board):
        # create game status
        self.game_status = GameStatus(init_board, len(players))
        self.players = players
        for player in players:
            player.set_game_status(self.game_status)
        self.choose_initial_destination_cards()
        self.run()

    def choose_initial_destination_cards(self):
        for _ in self.players:
            self.draw_destination_card_routine()
            self.game_status.end_turn()

    def draw_destination_card_routine(self):
        player = self.players[self.game_status.current_player]
        # draw 3 destination cards
        destination_card_pool = self.game_status.draw_destination_cards_phase_1()
        # choose 2 destination cards
        chosen_dc_index = player.choose_destination_cards(
            destination_card_pool, self.game_status.current_turn >= 0
        )
        # add chosen destination cards to player's destination cards
        self.game_status.draw_destination_cards_phase_2(chosen_dc_index)

    def run(self):
        while not self.game_status.game_over:
            player = self.players[self.game_status.current_player]
            action = player.get_action()

            if action.action_type == PlayerAction.DRAW_DESTINATION:
                self.draw_destination_card_routine()
            elif action.action_type == PlayerAction.DRAW_TRANSPORT:
                self.game_status.draw_transport_cards(action.args)
            elif action.action_type == PlayerAction.BUILD:
                self.game_status.build_on_link(action.args[0], action.args[1])

            self.game_status.end_turn()
