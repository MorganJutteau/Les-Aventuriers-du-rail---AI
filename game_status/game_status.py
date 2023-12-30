from point_counter import PointCounter


class GameStatus:
    def __init__(self, init_board, number_of_players):
        self.board = init_board

        # TODO: initialize these
        self.transport_deck = None
        self.destination_deck = None
        self.players_hands = [[] for _ in range(number_of_players)]
        self.players_destination_cards = [[] for _ in range(number_of_players)]
        self.current_player = 0
        self.point_counter = PointCounter(number_of_players)

    def build_on_link(self, node_a, node_b):
        # TODO : implement legality check and update player hand
        self.board.build_on_link(node_a, node_b, self.current_player)
        self.point_counter.on_build(self.current_player, node_a, node_b, self.board)

    def draw_transport_card(self, player):
        # TODO : implement
        pass

    def draw_destination_card(self, player):
        # TODO : implement
        pass

    def end_turn(self):
        self.current_player = (self.current_player + 1) % len(self.player_data)
