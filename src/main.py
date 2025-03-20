import sys
# Add content root to your path
sys.path.append('C:/Users/pawel/Desktop/Learning/max_flow_solver')

if __name__ == "__main__":
    import os

    from src.config.config import Config

    from src.solvers.ford_fulkerson import FordFulkersonDfsSolver
    from src.solvers.edmond_karp import EdmondKarpSolver
    from src.solvers.capacity_scaling import CapacityScalingSolver
    from src.solvers.dinics import DinicsSolver

    from src.utils.visuals import visualize_points_and_flows

    cwd = os.path.dirname(os.getcwd())

    config = Config()

    # Initialize MaxFlow solver class

    # solver = FordFulkersonDfsSolver(config)
    # solver = EdmondKarpSolver(config)
    # solver = CapacityScalingSolver(config)
    solver = DinicsSolver(config)

    # Create graph
    solver.add_edges()

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

    output_path = f"{config.output_image_folder}/{config.input_file_path.split('/')[-1].split('.')[-2]}_flow_chart.png"

    visualize_points_and_flows(DG, pos, output_path)
