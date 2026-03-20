import random


def parse_input(file):
    with open(file, "r") as f:
        lines = [line.strip() for line in f]
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


print(parse_input("input_format2"))


def count_weights(edges, partition):
    result = 0
    for v1, v2, value in edges:
        result += value * partition[v1] * (1 - partition[v2]) + value * partition[
            v2
        ] * (1 - partition[v1])
    return result


def maxcut(vertices, edges):
    maximum_cut = 0
    for _ in range(1000):
        partition = {vertice: random.choice([0, 1]) for vertice in vertices}

        result = count_weights(edges, partition)
        maximum_cut = max(maximum_cut, result)
    return maximum_cut


# print(maxcut(*parse_input("input_format2")))


def local_search_maxcut(vertices, edges, graph):
    print(vertices)
    partition = {vertice: random.choice([0, 1]) for vertice in vertices}

    change = False
    while not change:
        change = False
        for vertice in vertices:
            new_result = 0
            for v, value in graph[vertice]:
                if partition[vertice] != partition[v]:
                    new_result += value
                else:
                    new_result -= value
            # print(vertice, new_result)
            if new_result > 0:
                continue
            else:
                partition[vertice] = 1 - partition[vertice]
                change = True
    result = count_weights(edges, partition)
    return result


# print(local_search_maxcut(*parse_input("input_format2")))


def greedy_maxcut(vertices, edges, graph):
    S = set()
    T = set()
    vertices = list(vertices)
    print(vertices)
    weight_S = [0] * len(vertices)
    weight_T = [0] * len(vertices)

    S.add(vertices[0])
    for v in vertices[1:]:
        weight_S[vertices.index(v)] = sum(value for u, value in graph[v] if u in S)
        weight_T[vertices.index(v)] = sum(value for u, value in graph[v] if u in T)
        print(v, weight_S[vertices.index(v)], weight_T[vertices.index(v)])
        if weight_S[vertices.index(v)] >= weight_T[vertices.index(v)]:
            T.add(v)
        else:
            S.add(v)
    result = count_weights(edges, {v: 0 if v in S else 1 for v in vertices})
    return result


print(greedy_maxcut(*parse_input("input_format2")))
