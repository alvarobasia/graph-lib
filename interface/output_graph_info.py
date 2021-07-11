def print_graph_info(info):
    print(
        f"Grau máximo: {info['max_degree']['n']} \t Vértice: {info['max_degree']['v']}")
    print(
        f"Grau mínimo: {info['min_degree']['n']} \t Vértice: {info['min_degree']['v']}")
    print(f"Grau médio: {info['avg']}")
    print("Frequência relativa:")
    for i, v in enumerate(info['freq']):
        if v > 0:
            print(f"Grau {i}: {v}")
