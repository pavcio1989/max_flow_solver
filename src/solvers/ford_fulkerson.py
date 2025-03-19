from src.solvers.base import NetworkFlowBaseSolver


INFINITY = 1000000


class FordFulkersonDfsSolver(NetworkFlowBaseSolver):
    def __init__(self, n, s, t):
        super().__init__(n, s, t)

    def solve(self):
        flag = True
        while flag:
            f = self.dfs(self.s, INFINITY)
            self.visited_token += 1
            self.max_flow += f
            if f == 0:
                flag = False

    def dfs(self, node, flow):
        # At sink node, return augmented path flow
        if node == self.t:
            return flow

        # Mark the current node as visited
        self.visit(node)

        for edge in self.graph[node]:
            if edge.get_remaining_capacity() > 0 and not self.is_visited(edge.end):
                bottleneck = self.dfs(edge.end, min(flow, edge.get_remaining_capacity()))

                # Augment flow with bottleneck value
                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
        return 0
