import random


def parse_input(file):
    with open(file, "r") as f:
        lines = [line.strip("\n\t") for line in f]
        vertices = set()
        edges = []
        type = None

        for line in lines:
            if line == "V":
                type = "V"
                continue
            elif line == "E":
                type = "E"
                continue
            if type == "V":
                vertice = line.strip("()")
                vertices.add(vertice)
            elif type == "E":
                parts = line.split("-")
                v1 = parts[0].strip("()")
                v2 = parts[1].strip("()")
                value = int(parts[2])
                edges.append((v1, v2, value))

        graph = {v: [] for v in vertices}
        for v1, v2, value in edges:
            graph[v1].append((v2, value))
            graph[v2].append((v1, value))

        return vertices, edges, graph


print(parse_input("input_format"))


def maxcut(vertices, edges, graph):
    maximum_cut = 0
    for i in range(1000):
        partition = {vertice: random.choice([0, 1]) for vertice in vertices}

        result = 0
        for v1, v2, value in edges:
            result += value * partition[v1] * (1 - partition[v2]) + value * partition[
                v2
            ] * (1 - partition[v1])
        maximum_cut = max(maximum_cut, result)
    return maximum_cut


# print(maxcut(*parse_input("input_format")))


def local_search_maxcut(vertices, edges, graph):
    partition = {vertice: random.choice([0, 1]) for vertice in vertices}
    result = 0
    for v1, v2, value in edges:
        result += value * partition[v1] * (1 - partition[v2]) + value * partition[
            v2
        ] * (1 - partition[v1])

    improved = True
    while improved:
        improved = False
        for vertice in vertices:
            partition[vertice] = 1 - partition[vertice]
            new_result = 0
            for v1, v2, value in edges:
                new_result += value * partition[v1] * (
                    1 - partition[v2]
                ) + value * partition[v2] * (1 - partition[v1])
            if new_result > result:
                result = new_result
                improved = True
            else:
                partition[vertice] = 1 - partition[vertice]
            print(vertice, new_result, result)
    return result


print(local_search_maxcut(*parse_input("input_format")))
