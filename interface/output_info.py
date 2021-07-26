def print_connect_info(name, info):
    max_connect = max(info)
    result = [0 for _ in range(max_connect)]
    for v in info:
        result[v - 1] = result[v - 1] + 1

    with open(name, "w") as fd:
        fd.write(f'Componentes conexas: {max_connect}\n')
        fd.write(f'Maior componente: {max(result)}\n')
        fd.write(f'Menor componente: {min(result)}\n')
        for v in result:
            word = 'vértices'
            if v == 1:
                word = 'vértice'
            fd.write(f'=> {v } {word}\n')
