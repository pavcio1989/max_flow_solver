from base import NetworkFlowSolverBase


class FordFulkersonDfsSolver(NetworkFlowSolverBase):
    def __init__(self, n, s, t):
        super().__init__(n, s, t)
