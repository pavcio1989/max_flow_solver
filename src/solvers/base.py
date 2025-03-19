from abc import abstractmethod
from collections import defaultdict
import networkx as nx

from src.entities.edges import Edge
from src.config.config import Config
from src.data_manager.data_loader import DataLoader


class NetworkFlowBaseSolver:
    solved = False
    visited_token = 1
    visited = []
    max_flow = 0
    graph = defaultdict(list)
    directed_graph = None

    def __init__(self, config: Config):
        self.n = config.node_count
        self.s = config.source_id
        self.t = config.sink_id
        self.config = config
        self.visited = [0] * self.n

    @abstractmethod
    def solve(self):
        pass

    def add_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])

    def add_edge(self, start_node, end_node, capacity):
        if capacity <= 0:
            raise Exception("Forward edge capacity <=0")
        edge1 = Edge(start_node, end_node, capacity)
        edge2 = Edge(end_node, start_node, 0)

        edge1.residual = edge2
        edge2.residual = edge1

        self.graph[start_node].append(edge1)
        self.graph[end_node].append(edge2)

    def get_simple_graph(self):
        self.execute()
        return self.graph

    def get_directed_graph(self):
        self.execute()

        # Create empty NX directed graph
        dg = nx.DiGraph()

        # Fill graph with nodes and edges
        for node in self.graph:
            node_type = "middle"
            if node == self.s:
                node_type = "source"
            if node == self.t:
                node_type = "sink"
            dg.add_node(node, type=node_type)

            edges = self.graph[node]
            for edge in edges:
                dg.add_edge(edge.start, edge.end, flow=edge.flow, capacity=edge.capacity,
                            is_residual=edge.is_residual())

        pos = nx.spring_layout(dg, seed=1237)

        self.directed_graph = dg

        return self.directed_graph, pos

    def get_max_flow(self):
        self.execute()
        return self.max_flow

    def execute(self):
        if self.solved:
            return
        self.solved = True
        self.solve()

    # Mark node 'i' as visited
    def visit(self, i: int):
        self.visited[i] = self.visited_token

    def is_visited(self, i: int):
        return self.visited[i] == self.visited_token

    def mark_all_nodes_as_unvisited(self):
        self.visited_token += 1
