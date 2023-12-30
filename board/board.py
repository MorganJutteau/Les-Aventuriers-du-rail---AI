import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from utilities.unordered_pair_hashtable import UnorderedPairHashtable


class Board:
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes
        self.nodes = []
        self.adjacency_matrix = np.zeros(
            (number_of_nodes, number_of_nodes), dtype=int
        )  # at entry [i, j], 0 means no link between nodes with id i and j, 1 means link
        self.links = (
            UnorderedPairHashtable()
        )  # dictionary of links, key is tuple of node ids, value is link object that stores data about the link

    def add_node(self, node):
        node.set_id(len(self.nodes))
        self.nodes.append(node)

    def add_link(self, link):
        # link is an object of class Link
        self.links.add(link.node_1.id, link.node_2.id, link)
        self.adjacency_matrix[link.node_1.id, link.node_2.id] = 1
        self.adjacency_matrix[link.node_2.id, link.node_1.id] = 1
        self.nodes[link.node_1.id].neighbors.append(link.node_2)
        self.nodes[link.node_2.id].neighbors.append(link.node_1)

    def build_on_link(self, id_a, id_b):
        # id_a and id_b are the ids of the nodes that are linked
        link = self.links.get(id_a, id_b)
        link.on_built()

    def __str__(self) -> str:
        string = "##### NODE NAMES #####\n"
        for node in self.nodes:
            string += str(node.id) + " : " + str(node.name) + "\n"

        # print adjacency matrix
        string += "\n"
        string += "##### ADJACENCY MATRIX #####\n"
        string += str(self.adjacency_matrix)
        string += "\n"
        string += "\n"
        # print links

        string += "##### LINKS #####\n"
        for link in self.links.table:
            string += str(link) + " : " + str(self.links.table[link]) + "\n"
        return string
