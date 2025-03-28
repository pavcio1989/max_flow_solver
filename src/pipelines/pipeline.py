import logging

from src import solvers
from src.config.config import Config
from src.pipelines.names import MFSSolver
from src.utils.visuals import visualize_points_and_flows


logger = logging.getLogger('mfs')


class Pipeline:
    def __init__(self, config: Config):
        self.solvers = config.solvers
        self.max_flows = {}
        self._output_image_path = f"{config.output_image_folder}/{config.input_file_path.split('/')[-1].split('.')[-2]}_flow_chart.png"
        self._generate_report = config.generate_report
        self.config = config

    def run(self):
        for solver_name in self.solvers:
            if self.solvers[solver_name]:
                logger.info(f"Max Flow solver: {solver_name} | In scope: YES")

                # Initialize MaxFlow solver class
                solver: solvers.NetworkFlowBaseSolver = getattr(solvers, MFSSolver[solver_name].value)(self.config)

                # Create graph
                solver.add_edges()

                # Get maximum flow value
                logger.info(f"Maximum flow is: {solver.get_max_flow()}")

                # Get result graph
                result_graph = solver.get_simple_graph()

                # Display all edges of result graph
                for node in result_graph:
                    edges = result_graph[node]
                    for edge in edges:
                        print(edge)

                # Visualise network flow graph
                dg, pos = solver.get_directed_graph()

                visualize_points_and_flows(dg, pos, self._output_image_path)
            else:
                logger.info(f"Max Flow solver: {solver_name} | In scope: NO")
