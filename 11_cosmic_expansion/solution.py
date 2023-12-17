import numpy as np


class Universe:
    def __init__(self, map_of_the_universe: np.array):
        self._map = map_of_the_universe
        self._map_expanded = self._expand()

    def _expand(self):
        expanded_rows = []
        for row in range(self._map.shape[0]):
            expanded_rows.append(self._map[row, :])
            if np.all(self._map[row, :] == '.'):
                expanded_rows.append(self._map[row, :])
        expanded_rows = np.array(expanded_rows)
        expanded_cols = []
        for col in range(expanded_rows.shape[1]):
            expanded_cols.append(expanded_rows[:, col])
            if np.all(expanded_rows[:, col] == '.'):
                expanded_cols.append(expanded_rows[:, col])

        return np.array(expanded_cols).T

    def galaxy_indices(self):
        pass

    def lengths_of_shortest_paths(self):
        pass


def load_data(filename):
    with open(filename, 'r') as file:
        data = []
        for row in file:
            data.append([col for col in row.strip()])
    return Universe(np.array(data))


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
