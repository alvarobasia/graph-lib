def print_graph_info(name, info):
    with open(name, "w") as fd:
        fd.write(
            f"Grau máximo: {info['max_degree']['n']} \t Vértice: {info['max_degree']['v']}\n")
        fd.write(
            f"Grau mínimo: {info['min_degree']['n']} \t Vértice: {info['min_degree']['v']}\n")
        fd.write(f"Grau médio: {info['avg']}\n")
        fd.write("Frequência relativa:\n")
        for i, v in enumerate(info['freq']):
            if v > 0:
                fd.write(f"Grau {i}: {v}\n")
