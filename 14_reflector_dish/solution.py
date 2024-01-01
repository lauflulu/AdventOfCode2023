import re


class Platform:
    def __init__(self, platform):
        self.platform = platform
        self.rotate_right()

    def rotate_right(self):
        n_rows = len(self.platform)
        n_cols = len(self.platform[0])
        rotated_platform = ['' for _ in range(n_rows)]
        for r in reversed(range(n_rows)):
            for c in range(n_cols):
                rotated_platform[c] += self.platform[r][c]
        self.platform = rotated_platform

    def tilt(self):
        """Sort all O to the right until they reach # or border."""
        self.platform = [self._tilt_row(row) for row in self.platform]

    def _tilt_row(self, row: str) -> str:
        row = [c for c in row]
        n = len(row)
        for _ in range(n):
            fully_sorted = True
            for i in range(n-1):
                if row[i] == 'O' and row[i+1] == '.':
                    fully_sorted = False
                    row[i] = '.'
                    row[i + 1] = 'O'
            if fully_sorted:
                break
        return "".join(row)

    def result(self):
        self.tilt()
        return sum([m.start()+1 for row in self.platform for m in re.finditer(r'O', row)])


def load_data(filename):
    with open(filename, 'r') as file:
        return Platform([row.strip() for row in file])


def get_result(platfrom: Platform):
    return platfrom.result()


def get_result_2(data):
    pass


def main():
    data = load_data("data.txt")
    print(get_result(data))
    print(get_result_2(data))


if __name__ == '__main__':
    main()
