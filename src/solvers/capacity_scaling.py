from src.solvers.base import NetworkFlowBaseSolver
from src.entities.edges import Edge


INFINITY = 1000000


class CapacityScalingSolver(NetworkFlowBaseSolver):
    delta: int = 0

    def __init__(self, config):
        super().__init__(config)

    def add_edge(self, start_node, end_node, capacity):
        super().add_edge(start_node, end_node, capacity)
        self.delta = max(self.delta, capacity)

    def solve(self):
        # Start delta at the largest power of 2
        self.delta = 2 ** (self.delta.bit_length() - 1)

        while self.delta > 0:
            flow = INFINITY
            while flow != 0:
                self.mark_all_nodes_as_unvisited()
                flow = self.dfs(self.s, INFINITY)
                self.max_flow += flow
            self.delta = int(self.delta / 2)

    def dfs(self, node, flow):
        # At sink node, return augmented path flow
        if node == self.t:
            return flow

        # Mark the current node as visited
        self.visit(node)

        for edge in self.graph[node]:
            cap = edge.get_remaining_capacity()

            if cap >= self.delta and not self.is_visited(edge.end):
                bottleneck = self.dfs(edge.end, min(flow, cap))

                # Augment flow with bottleneck value
                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck

        return 0
