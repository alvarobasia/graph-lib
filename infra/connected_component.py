from typing import List
from domain.Graph import Graph


class Connected_Component:
    result: List[int]
    graph: Graph
    tag: int
    representation: bool
    search: bool

    def __init__(self, graph: Graph, representation: bool, search: bool):
        self.tag = 0
        self.graph = graph
        self.result = [0 for i in range(graph.nodes_number + 1)]
        self.representation = representation
        self.search = search

    def get_info(self):
        if self.representation:
            if self.search:
                return self.__get_connected_component_list_deep()
            else:
                self.__get_connected_component_list_wide()
        else:
            if self.search:
                self.__get_connected_component_matrix_deep()
            else:
                self.__get_connected_component_matrix_wide()

    def __get_connected_component_list_deep(self):
        graph = self.graph.get_list_representation()
        for u in range(len(graph)):
            if self.result[u] == 0:
                self.tag = self.tag + 1
                self.__deep_search_list_connect(u, graph)
        return self.result

    def __get_connected_component_matrix_deep(self):
        pass

    def __get_connected_component_list_wide(self):
        pass

    def __get_connected_component_matrix_wide(self):
        pass

    def __deep_search_list_connect(self, el, graph):
        self.result[el] = self.tag
        for v in graph[el]:
            if self.result[v[0]] == 0:
                self.__deep_search_list_connect(v[0], graph)
