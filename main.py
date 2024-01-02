from game_manager import GameManager
from player_package.human_player import HumanPlayer
from utilities import test_board_constructors

if __name__ == "__main__":
    # create game manager
    players = [HumanPlayer(), HumanPlayer()]
    init_board = test_board_constructors.four_cities()
    game_manager = GameManager(players, init_board)
