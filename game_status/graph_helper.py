from collections import defaultdict
import heapq as heap


class GraphHelper:
    def calculate_eccentricity(u, board, player):
        # Calculates the eccentricity of a node u.
        # This is the length of the shortest path from u to the farthest node from u

        _, nodeCosts = GraphHelper.dijkstra(board, u, player)
        return max(nodeCosts.values()), nodeCosts

    def get_connected_components_representatives(board, player):
        # get one starting vertex per connected component
        visited = [False for _ in range(board.number_of_nodes)]
        starting_vertices = []
        for i in range(board.number_of_nodes):
            if not visited[i]:
                starting_vertices.append(i)
                visited[i] = True
                queue = [i]
                while len(queue) > 0:
                    next_queue = []
                    for v in queue:
                        for w in board.nodes[v].neighbors:
                            if (
                                board.get_link(v, w.id).owner == player
                                and not visited[w.id]
                            ):
                                visited[w.id] = True
                                next_queue.append(w.id)
                    queue = next_queue
        return starting_vertices

    def calculate_connected_component_diameter(board, player, starting_node):
        # Implementation of the iFUB algorithm for calculating the diameter of a connected component
        # https://pages.di.unipi.it/ferragina/dott2014/diameter.pdf

        start_eccentricity, nodeCosts = GraphHelper.calculate_eccentricity(
            starting_node, board, player
        )
        # organize nodes by fringes (distance from starting node)
        fringes = defaultdict(list)
        for node in nodeCosts:
            fringes[nodeCosts[node]].append(node)
        # calculate diameter

        i = start_eccentricity
        ub = 2 * start_eccentricity
        lb = start_eccentricity
        while ub > lb:
            if len(fringes[i]) > 0:
                # Bi(u) is the maximum eccentricity of a node in the fringe i
                Bi = max(
                    [
                        GraphHelper.calculate_eccentricity(u, board, player)[0]
                        for u in fringes[i]
                    ]
                )
                if max(lb, Bi) > 2 * (i - 1):
                    return max(lb, Bi)
                else:
                    lb = max(lb, Bi)
                    ub = 2 * (i - 1)
            i -= 1
        return lb

    def calculate_longest_path_for_player(board, player):
        # NB : Actually, this is not a longest path, but a diameter

        # Calculates the longest path for a player
        # This is the longest path between any two nodes that are owned by the player
        # Returns the length of the path and the nodes that are part of the path
        starting_vertices = GraphHelper.get_connected_components_representatives(
            board, player
        )
        max_diameter = 0
        for starting_node in starting_vertices:
            diameter = GraphHelper.calculate_connected_component_diameter(
                board, player, starting_node
            )
            max_diameter = max(max_diameter, diameter)
        return max_diameter

    def dijkstra(board, starting_node, player):
        visited = set()
        parentsMap = {}
        pq = []
        nodeCosts = defaultdict(lambda: float("inf"))
        nodeCosts[starting_node] = 0
        heap.heappush(pq, (0, starting_node))

        while pq:
            # go greedily by always extending the shorter cost nodes first
            _, node = heap.heappop(pq)
            visited.add(node)
            for n in board.nodes[node].neighbors:
                adj_node = n.id
                if (
                    adj_node in visited
                    or board.get_link(node, adj_node).owner != player
                ):
                    continue
                weight = board.get_link(node, adj_node).weight
                newCost = nodeCosts[node] + weight
                if nodeCosts[adj_node] > newCost:
                    parentsMap[adj_node] = node
                    nodeCosts[adj_node] = newCost
                    heap.heappush(pq, (newCost, adj_node))

        return parentsMap, nodeCosts
