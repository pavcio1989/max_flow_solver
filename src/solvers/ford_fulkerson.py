from src.solvers.base import NetworkFlowSolverBase


INFINITY = 1000000


class FordFulkersonDfsSolver(NetworkFlowSolverBase):
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
        self.visited[node] = self.visited_token

        edges = self.graph[node]

        for edge in edges:
            if edge.get_remaining_capacity() > 0 and self.visited[edge.end] != self.visited_token:
                bottleneck = self.dfs(edge.end, min(flow, edge.get_remaining_capacity()))

                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
        return 0
