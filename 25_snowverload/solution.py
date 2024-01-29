import numpy as np


def load_data(filename):
    with open(filename, "r") as f:
        nodes = []
        for line in f:
            neighbors, node = _parse(line)
            for n in [node] + neighbors:
                if n not in nodes:
                    nodes.append(n)
        adjacency_matrix = np.zeros((len(nodes), len(nodes)))
        for line in open(filename, "r"):
            neighbors, node = _parse(line)
            for n in neighbors:
                adjacency_matrix[nodes.index(node), nodes.index(n)] = 1
    return adjacency_matrix + adjacency_matrix.T


def _parse(line):
    node, neighbors = line.split(":")
    node = node.strip()
    neighbors = [n.strip() for n in neighbors.strip().split(" ")]
    return neighbors, node


def get_result(data):
    pass


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
