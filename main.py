from utils.get_correct_values import get_correct_values
from domain.Graph import Graph
from infra.graph_info import Graph_info
from infra.graph_search import Graph_Search
from infra.connected_component import Connected_Component
from utils.representation_type import Representation
from utils.search_type import Search_type
s = []
with open("teste.txt", "r") as fd:
    for line in fd:
        s.append(line.strip())

result = get_correct_values(s)

graph = Graph(result['nodes'], result['edges'], result['values'])

g = Connected_Component(
    graph, Representation.ADJACENCY_MATRIX, Search_type.DEEP_SEARCH)
print(g.get_info())
