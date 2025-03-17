class NetworkFlowSolverBase:
    def __init__(self, n, s, t):
        self.n = n
        self.s = s
        self.t = t

    def add_edge(self, start_node, end_node, capacity):
        pass

    def get_max_flow(self):
        pass

    def get_graph(self):
        pass
