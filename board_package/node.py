class Node:
    def __init__(self, name, id=-1) -> None:
        self.id = id  # number of the node in the graph : a priori useless here but good to have
        self.name = name
        self.neighbors = []

    def set_id(self, id):
        self.id = id
