class Link:
    def __init__(self, node_a, node_b, length, color) -> None:
        # node_1 must be  is the node with the smallest id
        # this convention avoids considering two links to be different
        # if they are the same but with the nodes in the other order
        if node_a.id < node_b.id:
            self.node_1 = node_a
            self.node_2 = node_b
        else:
            self.node_2 = node_b
            self.node_1 = node_a

        self.length = length  # number of wagon cards needed to claim this link
        self.color = color  # color of the wagon cards needed to claim this link
        self.occupied = False  # True if a player has claimed this link
        self.owner = None  # player who claimed this link

    def on_built(self, builder):
        self.occupied = True
        self.owner = builder

    def __str__(self) -> str:
        return f"length: {self.length}, color: {self.color}, owner: {self.owner}"
