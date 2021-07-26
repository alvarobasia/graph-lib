def write_search(name: str, info):
    info.sort(key=lambda x: x[1])
    with open(name, "w") as fd:
        fd.write("#vertice:nível\n")
        for v in info:
            fd.write(f'{v[0]}:{v[1]}\n')
