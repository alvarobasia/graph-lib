def write_search(name: str, info):
    info.sort(key=lambda x: x[1])
    with open(name, "x") as fd:
        fd.write("#vertice:nível\n")
        for v in info:
            fd.write(f'{v[1]}:{v[0]}\n')
