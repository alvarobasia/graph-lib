from typing import List, Tuple
import numpy as np
from scipy.sparse import *
from scipy import *


class Graph:
    nodes_number: int
    edges_number: int
    values: List[List[int]]

    def __init__(self, nodes_number: int, edges_number: int, values: List[List[int]]) -> None:
        self.edges_number = edges_number
        self.nodes_number = nodes_number
        self.values = values

    def get_matrix_representation(self) -> List[List[int]]:
        # list = [[]for x in range(self.nodes_number + 1)]
        # for v in range(len(list)):
        #     list[v] = [0 for x in range(self.nodes_number + 1)]
        f = csc_matrix((self.nodes_number, self.nodes_number),
                       dtype=int8).toarray()
        for v in self.values:
            f[v[0]][v[1]] = v[2]
            f[v[1]][v[0]] = v[2]
        return f

    def get_list_representation(self) -> List[Tuple[int]]:
        list = [[] for x in range(self.nodes_number)]
        for v in self.values:
            list[v[0]].append((v[1], v[2]))
            list[v[1]].append((v[0], v[2]))
        return list
