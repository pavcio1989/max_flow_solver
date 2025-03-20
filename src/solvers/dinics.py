from collections import deque

from src.solvers.base import NetworkFlowBaseSolver
from src.entities.edges import Edge


INFINITY = 1000000


class DinicsSolver(NetworkFlowBaseSolver):
    def __init__(self, config):
        super().__init__(config)
        self.level = []
        self.next = []

    def solve(self):
        while self.bfs():
            next_edge = [0] * self.n

            flow = self.dfs(self.s, next_edge, INFINITY)

            while flow != 0:
                self.max_flow += flow
                flow = self.dfs(self.s, next_edge, INFINITY)

    def bfs(self) -> bool:
        self.level = [-1] * self.n

        # Initialize BFS deque (queue)
        q = deque()

        # Add source node to deque
        q.append(self.s)
        self.level[self.s] = 0

        while len(q) > 0:
            node = q.popleft()

            for edge in self.graph[node]:
                cap = edge.get_remaining_capacity()
                if cap > 0 and self.level[edge.end] == -1:
                    self.level[edge.end] = self.level[node] + 1
                    q.append(edge.end)

        return self.level[self.t] != -1

    def dfs(self, at: int, next_edge: list, flow: float) -> float:
        if at == self.t:
            return flow
        num_edges = len(self.graph[at])

        while next_edge[at] < num_edges:
            edge: Edge = self.graph[at][next_edge[at]]
            cap = edge.get_remaining_capacity()

            if cap > 0 and self.level[edge.end] == self.level[at] + 1:
                bottleneck = self.dfs(edge.end, next_edge, min(flow, cap))

                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
            next_edge[at] += 1

        return 0
