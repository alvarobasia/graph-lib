from typing import List, Tuple
import numpy as np


class Graph:
    nodes_number: int
    edges_number: int
    values: List[List[int]]
    nodes_number: int

    def __init__(self, nodes_number: int, edges_number: int, values: List[List[int]]) -> None:
        self.edges_number = edges_number
        self.nodes_number = nodes_number
        self.values = values
        self.nodes_number = np.max([x[0:2] for x in values])

    def get_matrix_representation(self) -> List[List[int]]:
        matrix = [[0 for x in range(self.nodes_number + 1)]
                  for x in range(self.nodes_number + 1)]
        for v in self.values:
            matrix[v[0]][v[1]] = v[2]
            matrix[v[1]][v[0]] = v[2]
        return matrix

    def get_list_representation(self) -> List[Tuple[int]]:
        list = [[] for x in range(self.nodes_number + 1)]
        for v in self.values:
            list[v[0]].append((v[1], v[2]))
            list[v[1]].append((v[0], v[2]))
        return list
