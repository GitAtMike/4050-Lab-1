from collections import defaultdict
from typing import Dict, List, Tuple, Optional
from graph_representations import Graph

# Kept implementation basic, but still shows as a hybrid

class HybridGraph(Graph):
    """
    Hybrid graph:
    - Uses adjacency lists normally
    - Switches to small adjacency matrices for locally dense nodes
    """

    def __init__(self, density_threshold: float = 0.1):
        super().__init__()
        self.density_threshold = density_threshold

        # Always keep adjacency list
        self.adj_list: Dict[int, List[Tuple[int, float]]] = defaultdict(list)

        # Dense node storage
        self.dense_nodes = set()
        self.matrix_blocks: Dict[int, Dict[int, float]] = defaultdict(dict)

    def add_edge(self, from_id: int, to_id: int, weight: float) -> None:
        # Always store in list
        self.adj_list[from_id].append((to_id, weight))
        self.adj_list[to_id].append((from_id, weight))
        self.num_edges += 1

        # Check if node becoming dense
        self._check_density(from_id)
        self._check_density(to_id)

        # If dense, also store in mini-matrix
        if from_id in self.dense_nodes:
            self.matrix_blocks[from_id][to_id] = weight
        if to_id in self.dense_nodes:
            self.matrix_blocks[to_id][from_id] = weight

    def _check_density(self, node_id: int):
        degree = len(self.adj_list[node_id])
        n = max(1, len(self.nodes))
        density = degree / n

        if density > self.density_threshold:
            self.dense_nodes.add(node_id)

    def get_neighbors(self, node_id: int) -> List[Tuple[int, float]]:
        return self.adj_list[node_id]

    def has_edge(self, from_id: int, to_id: int) -> bool:
        # Use matrix if dense
        if from_id in self.dense_nodes:
            return to_id in self.matrix_blocks[from_id]

        # Otherwise list scan
        return any(n == to_id for n, _ in self.adj_list[from_id])

    def get_edge_weight(self, from_id: int, to_id: int) -> Optional[float]:
        if from_id in self.dense_nodes:
            return self.matrix_blocks[from_id].get(to_id)

        for n, w in self.adj_list[from_id]:
            if n == to_id:
                return w
        return None

    def get_memory_bytes(self) -> int:
        # Rough estimate
        list_mem = self.num_edges * 2 * 16
        matrix_mem = sum(len(v) for v in self.matrix_blocks.values()) * 16
        return list_mem + matrix_mem
