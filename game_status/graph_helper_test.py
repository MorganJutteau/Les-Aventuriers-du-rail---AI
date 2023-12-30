import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graph_helper import GraphHelper
import board

# create a linear board
map = board.Board(6)
map.add_node(board.Node("Paris"))
map.add_node(board.Node("Berlin"))
map.add_node(board.Node("London"))
map.add_node(board.Node("Madrid"))
map.add_node(board.Node("Rome"))
map.add_node(board.Node("Moscow"))


map.add_link(board.Link(map.nodes[0], map.nodes[1], 1, "red"))
map.add_link(board.Link(map.nodes[1], map.nodes[2], 1, "blue"))
map.add_link(board.Link(map.nodes[2], map.nodes[3], 1, "black"))
map.add_link(board.Link(map.nodes[3], map.nodes[4], 1, "black"))
map.add_link(board.Link(map.nodes[4], map.nodes[5], 1, "black"))

print(map)

# build links
map.build_on_link(0, 1, 0)
map.build_on_link(1, 2, 0)
map.build_on_link(2, 3, 0)
map.build_on_link(4, 5, 0)
map.build_on_link(3, 4, 1)

print(map)

print(GraphHelper.get_connected_components_representatives(map, 0))
print(GraphHelper.calculate_longest_path_for_player(map, 0))
