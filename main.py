from utils.search_type import Search_type
from utils.representation_type import Representation
from guppy import hpy
from utils.get_correct_values import get_correct_values
from domain.Graph import Graph
from infra.graph_info import Graph_info
from infra.graph_search import Graph_Search
from infra.connected_component import Connected_Component
from memory_profiler import profile
# from utils.representation_type import Representation
# from utils.search_type import Search_type
from interface.output_graph_info import print_graph_info
from interface.write_search import write_search
from interface.output_connect_info import print_connect_info
import time
import os
import psutil
pid = os.getpid()
python_process = psutil.Process(pid)
s = []
with open("as_graph.txt", "r") as fd:
    for line in fd:
        s.append(line.strip())

result = get_correct_values(s)

graph = Graph(result['nodes'], result['edges'], result['values'])
s = Graph_Search(graph, Representation.ADJACENCY_LIST)
f = []


for i in range(0, len(graph.get_list_representation())+1):
    f.append([i, s.search_deep(i)[-1]])

with open('teste.txt', "x") as fd:
    for g in f:
        fd.write(f'{g[0]}:{g[1]}\n')

# print(f'============>{y}')
# write_search('1000.txt', )
# p = Connected_Component(
#     graph, Representation.ADJACENCY_LIST, Search_type.WIDE_SEARCH)

# print_connect_info(p.get_info())
# print(python_process.memory_info()[0]/2.**30)
