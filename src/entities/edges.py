class Edge:
    flow: float = 0
    residual = None

    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity

    def is_residual(self):
        return self.capacity == 0

    def get_remaining_capacity(self):
        return self.capacity - self.flow

    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck

    def __str__(self):
        print(f"Edge {self.start} -> {self.end} | flow = {self.flow} \
        | capacity = {self.capacity} | is residual = {self.is_residual()}")
