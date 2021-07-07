from domain.Graph import Graph
from utils.representation_type import Representation


class Graph_Search:
    graph: Graph
    representation: Representation

    def __init__(self, graph: Graph, representation: Representation):
        self.graph = graph
        self.representation = representation

    def search_wide(self, el: int):
        if self.representation == Representation.ADJACENCY_LIST:
            return self.__search_wide_list(el)
        else:
            return self.__search_wide_matrix(el)

    def __search_wide_list(self, el: int):
        graph = self.graph.get_list_representation()
        desc = [0 for i in range(len(graph))]
        level = 0
        Q = [el]
        R = [[level, el]]
        desc[el] = 1
        while len(Q) != 0:
            level = level + 1
            u = Q.pop(0)
            for v in graph[u]:
                if desc[v[0]] == 0:
                    Q.append(v[0])
                    R.append([level, v[0]])
                    desc[v[0]] = 1
        return R

    def __search_wide_matrix(self, el: int):
        graph = self.graph.get_matrix_representation()
        desc = [0 for i in range(len(graph))]
        level = 0
        Q = [el]
        R = [[level, el]]
        desc[el] = 1
        while len(Q) != 0:
            level = level + 1
            u = Q.pop(0)
            for i, v in enumerate(graph[u]):
                if v != 0 and desc[i] == 0:
                    Q.append(i)
                    R.append([level, i])
                    desc[i] = 1
        return R

    def search_deep(self, el: int):
        if self.representation == 0:
            return self.__search_deep_list(el)
        else:
            return self.__search_deep_matrix(el)

    def __search_deep_list(self, el: int):
        graph = self.graph.get_list_representation()
        desc = [0 for i in range(len(graph))]
        S = [el]
        level = 0
        R = [[level, el]]
        desc[el] = 1
        level = level + 1
        while len(S) != 0:
            u = S[-1]
            pop = True
            for v in graph[u]:
                if desc[v[0]] == 0:
                    pop = False
                    S.append(v[0])
                    R.append([level, v[0]])
                    desc[v[0]] = 1
                    break
            if pop:
                level = level + 1
                S.pop()
        return R

    def __search_deep_matrix(self, el: int):
        graph = self.graph.get_matrix_representation()
        desc = [0 for i in range(len(graph))]
        S = [el]
        level = 0
        R = [[level, el]]
        desc[el] = 1
        level = level + 1
        while len(S) != 0:
            u = S[-1]
            pop = True
            for i, v in enumerate(graph[u]):
                if v != 0 and desc[i] == 0:
                    pop = False
                    S.append(i)
                    R.append([level, i])
                    desc[i] = 1
                    break
            if pop:
                level = level + 1
                S.pop()
        return R
