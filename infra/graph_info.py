from domain.Graph import Graph
import numpy as np


class Graph_info:
    graph: Graph
    representation: bool

    def __init__(self, graph: Graph, representation: bool):
        self.graph = graph
        self.representation = representation

    def get_max_degree(self):
        result: int
        if self.representation:
            return self.__get_max_degree_list()
        else:
            return self.__get_max_degree_matrix()

    def __get_max_degree_list(self):
        graph = self.graph.get_list_representation()
        result = [0 for x in graph]
        for v in graph:
            for f in v:
                result[f[0]] = result[f[0]] + 1
        max_value = max(result)
        min_value = min(result)
        freq_relative = [0 for x in range(max_value + 1)]
        for value in result:
            freq_relative[value] = freq_relative[value] + 1
        freq_relative = [x / sum(freq_relative)
                         for x in freq_relative]
        return {'max_degree': {
            'n': max_value,
            'v': result.index(max_value)
        }, 'min_degree': {
            'n': min_value,
            'v': result.index(min_value)
        },
            'avg': sum(result) / len(result),
            'freq': freq_relative
        }

    def __get_max_degree_matrix(self):
        graph = self.graph.get_matrix_representation()
        result = [0 for x in graph]
        for v in graph:
            for f, l in enumerate(v):
                if l != 0:
                    result[f] = result[f] + 1
        print(result)
