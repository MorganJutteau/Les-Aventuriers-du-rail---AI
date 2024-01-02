from board_package.board import Board
from board_package.link import Link
from board_package.node import Node


def four_cities():
    paris = Node("Paris")
    berlin = Node("Berlin")
    london = Node("London")
    madrid = Node("Madrid")

    board = Board(4)
    board.add_node(paris)
    board.add_node(berlin)
    board.add_node(london)
    board.add_node(madrid)

    paris_berlin = Link(paris, berlin, 2, "red")
    paris_london = Link(paris, london, 1, "blue")
    paris_madrid = Link(paris, madrid, 1, "black")
    berlin_london = Link(berlin, london, 1, "black")

    board.add_link(paris_berlin)
    board.add_link(paris_london)
    board.add_link(paris_madrid)
    board.add_link(berlin_london)

    return board
