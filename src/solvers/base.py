from abc import abstractmethod
from collections import defaultdict

from src.entities.edges import Edge


class NetworkFlowSolverBase:
    solved = False
    visited_token = 1
    visited = []
    max_flow = 0
    graph = defaultdict(list)

    def __init__(self, n, s, t):
        self.n = n
        self.s = s
        self.t = t
        self.visited = [0] * n

    @abstractmethod
    def solve(self):
        pass

    def add_edge(self, start_node, end_node, capacity):
        if capacity <= 0:
            raise Exception("Forward edge capacity <=0")
        edge1 = Edge(start_node, end_node, capacity)
        edge2 = Edge(end_node, start_node, 0)

        edge1.residual = edge2
        edge2.residual = edge1

        self.graph[start_node].append(edge1)
        self.graph[end_node].append(edge2)

    def get_graph(self):
        self.execute()
        return self.graph

    def get_max_flow(self):
        self.execute()
        return self.max_flow

    def execute(self):
        if self.solved:
            return
        self.solved = True
        self.solve()
