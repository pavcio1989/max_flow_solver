import os

from src.solvers.ford_fulkerson import FordFulkersonDfsSolver
from src.solvers.edmond_karp import EdmondKarpSolver
from src.solvers.capacity_scaling import CapacityScalingSolver
from src.utils.visuals import visualize_points_and_flows

cwd = os.path.dirname(os.getcwd())

# Initialize graph parameters
# Number of nodes (source and sink inclusive)
n = 11

# Source and sink index
s = n - 2
t = n - 1
print(f"Source node: {s}")
print(f"Sink node: {t}")

# Initialize MaxFlow solver class
# solver = FordFulkersonDfsSolver(n, s, t)
# solver = EdmondKarpSolver(n, s, t)
solver = CapacityScalingSolver(n, s, t)

# Create graph
# Add edges from source
solver.add_edge(s, 0, 10)
solver.add_edge(s, 1, 5)
solver.add_edge(s, 2, 10)

# Add middle edges
solver.add_edge(0, 3, 10)
solver.add_edge(1, 2, 10)
solver.add_edge(2,5, 15)
solver.add_edge(3, 1, 2)
solver.add_edge(3, 6, 15)
solver.add_edge(4, 3, 3)
solver.add_edge(4, 1, 15)
solver.add_edge(5, 4, 4)
solver.add_edge(5, 8, 10)
solver.add_edge(6, 7, 10)
solver.add_edge(7, 4, 10)
solver.add_edge(7, 5, 7)

# Add edges to sink
solver.add_edge(6, t, 15)
solver.add_edge(8, t, 10)

# Get maximum flow value
print(f"Maximum flow is: {solver.get_max_flow()}")

# Get result graph
result_graph = solver.get_simple_graph()

# Display all edges of result graph
for node in result_graph:
    edges = result_graph[node]
    for edge in edges:
        print(edge)

# Visualise network flow graph
DG, pos = solver.get_directed_graph()

output_path = f"{cwd}/images/output/flow_chart.png"

visualize_points_and_flows(DG, pos, output_path)
