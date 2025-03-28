from enum import Enum


class MFSSolver(Enum):
    ford_fulkerson = "FordFulkersonDfsSolver"
    edmond_karp = "EdmondKarpSolver"
    capacity_scaling = "CapacityScalingSolver"
    dinics = "DinicsSolver"
