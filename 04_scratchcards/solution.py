class Card:

    def __init__(self, winning_numbers: tuple[int], scratch_numbers: tuple[int]):
        self.winning_numbers: tuple[int] = winning_numbers
        self.scratch_numbers: tuple[int] = scratch_numbers

    def value(self):
        pass


def load_data(filepath: str) -> list[Card]:
    with open(filepath, 'r') as file:
        return [_parse(line) for line in file]


def _parse(line: str):
    _, numbers = line.split(':')
    winning_numbers, scratch_numbers = numbers.split('|')
    return Card(_parse_numbers(winning_numbers), _parse_numbers(scratch_numbers))


def _parse_numbers(numbers: str):
    return tuple([int(number.strip()) for number in numbers.split(' ') if not number == ''])


def get_result(data) -> int:
    pass
