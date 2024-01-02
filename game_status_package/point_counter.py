from game_status_package.graph_helper import GraphHelper


class PointCounter:
    def __init__(self, number_of_players):
        self.points = [0 for _ in range(number_of_players)]
        self.point_table = [0, 1, 2, 4, 7, 10, 15]
        self.longest_path_bonus = 10

    def on_build(self, player, node_a, node_b, board):
        self.points[player] += self.point_table[board.get_link(node_a, node_b).weight]

    def get_points(self, player):
        return self.points[player]

    def apply_longest_path_bonus(self, board):
        longest_path_player = -1
        longest_path_length = 0
        for player in range(len(self.points)):
            longest_path_for_player = GraphHelper.calculate_longest_path_for_player(
                board, player
            )
            if longest_path_for_player > longest_path_length:
                longest_path_length = longest_path_for_player
                longest_path_player = player
        if longest_path_player != -1:
            self.points[longest_path_player] += self.longest_path_bonus
