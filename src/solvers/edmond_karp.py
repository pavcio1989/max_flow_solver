from collections import deque

from src.solvers.base import NetworkFlowBaseSolver
from src.entities.edges import Edge


INFINITY = 1000000


class EdmondKarpSolver(NetworkFlowBaseSolver):
    def __init__(self, n, s, t):
        super().__init__(n, s, t)

    def solve(self):
        flow = INFINITY
        while flow != 0:
            self.mark_all_nodes_as_unvisited()
            flow = self.bfs()
            self.max_flow += flow

    def bfs(self):
        # Initialize BFS deque (queue)
        q = deque()

        # Add source node to deque
        self.visit(self.s)
        q.append(self.s)

        # Perform BFS from source to sink
        prev: list[Edge] = [None] * self.n

        while len(q) > 0:
            node = q.popleft()
            if node == self.t:
                break
            for edge in self.graph[node]:
                cap = edge.get_remaining_capacity()
                if cap > 0 and not self.is_visited(edge.end):
                    self.visit(edge.end)
                    prev[edge.end] = edge
                    q.append(edge.end)

        # Sink not reachable
        if prev[self.t] is None:
            return 0

        # Find augmented path and bottleneck
        bottleneck = INFINITY

        edge = prev[self.t]
        while edge is not None:
            bottleneck = min(bottleneck, edge.get_remaining_capacity())
            edge = prev[edge.start]

        # Retrace augmented path and update flow values
        edge = prev[self.t]
        while edge is not None:
            edge.augment(bottleneck)
            edge = prev[edge.start]

        return bottleneck
