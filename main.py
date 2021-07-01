from utils.get_correct_values import get_correct_values
from domain.Graph import Graph
s = []
with open("teste.txt", "r") as fd:
    for line in fd:
        s.append(line.strip())

result = get_correct_values(s)

graph = Graph(result['nodes'], result['edges'], result['values'])
print(graph.get_matrix_representation())
