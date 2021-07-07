from typing import List
from domain.Graph import Graph
from utils.representation_type import Representation
from utils.search_type import Search_type


class Connected_Component:
    result: List[int]
    graph: Graph
    tag: int
    representation: Representation
    search: Search_type

    def __init__(self, graph: Graph, representation: Representation, search: Search_type):
        self.tag = 0
        self.graph = graph
        self.result = [0 for i in range(graph.nodes_number + 1)]
        self.representation = representation
        self.search = search

    def get_info(self):
        if self.representation == Representation.ADJACENCY_LIST:
            if self.search == Search_type.DEEP_SEARCH:
                return self.__get_connected_component_list_deep()
            else:
                return self.__get_connected_component_list_wide()
        else:
            if self.search == Search_type.DEEP_SEARCH:
                return self.__get_connected_component_matrix_deep()
            else:
                return self.__get_connected_component_matrix_wide()

    def __get_connected_component_list_deep(self):
        graph = self.graph.get_list_representation()
        for u in range(len(graph)):
            if self.result[u] == 0:
                self.tag = self.tag + 1
                self.__deep_search_list_connect(u, graph)
        return self.result

    def __get_connected_component_matrix_deep(self):
        graph = self.graph.get_matrix_representation()
        for u in range(len(graph)):
            if self.result[u] == 0:
                self.tag = self.tag + 1
                self.__deep_search_matrix_connect(u, graph)
        return self.result

    def __get_connected_component_list_wide(self):
        graph = self.graph.get_list_representation()
        for u in range(len(graph)):
            if self.result[u] == 0:
                self.tag = self.tag + 1
                self.__wide_search_list_connect(u, graph)
        return self.result

    def __get_connected_component_matrix_wide(self):
        graph = self.graph.get_matrix_representation()
        for u in range(len(graph)):
            if self.result[u] == 0:
                self.tag = self.tag + 1
                self.__wide_search_matrix_connect(u, graph)
        return self.result

    def __deep_search_list_connect(self, el, graph):
        self.result[el] = self.tag
        for v in graph[el]:
            if self.result[v[0]] == 0:
                self.__deep_search_list_connect(v[0], graph)

    def __deep_search_matrix_connect(self, el, graph):
        self.result[el] = self.tag
        for i, v in enumerate(graph[el]):
            if v != 0 and self.result[i] == 0:
                self.__deep_search_matrix_connect(i, graph)

    def __wide_search_list_connect(self, el, graph):
        self.result[el] = self.tag
        Q = [el]
        while len(Q) != 0:
            u = Q.pop(0)
            for v in graph[u]:
                if self.result[v[0]] == 0:
                    Q.append(v[0])
                    self.result[v[0]] = self.tag

    def __wide_search_matrix_connect(self, el, graph):
        self.result[el] = self.tag
        Q = [el]
        while len(Q) != 0:
            u = Q.pop(0)
            for i, v in enumerate(graph[el]):
                if v != 0 and self.result[i] == 0:
                    Q.append(i)
                    self.result[i] = self.tag
