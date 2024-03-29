import pytest

import solution

GAME_1 = [{'red': 4, 'green': 0, 'blue': 3}, {'red': 1, 'green': 2, 'blue': 6}, {'red': 0, 'green': 2, 'blue': 0}]
GAME_2 = [{'red': 0, 'green': 2, 'blue': 1}, {'red': 1, 'green': 3, 'blue': 4}, {'red': 0, 'green': 1, 'blue': 1}]
GAME_3 = [{'red': 20, 'green': 8, 'blue': 6}, {'red': 4, 'green': 13, 'blue': 5}, {'red': 1, 'green': 5, 'blue': 0}]
GAME_4 = [{'red': 3, 'green': 1, 'blue': 6}, {'red': 6, 'green': 3, 'blue': 0}, {'red': 14, 'green': 3, 'blue': 15}]
GAME_5 = [{'red': 6, 'green': 3, 'blue': 1}, {'red': 1, 'green': 2, 'blue': 2}]


def test_that_load_example_data_is_a_list_of_list_of_dicts():
    data = solution.load_data("example_data.txt")
    assert isinstance(data, list)
    assert isinstance(data[0], list)
    assert isinstance(data[0][0], dict)


@pytest.mark.parametrize("game, index", [(GAME_1, 0), (GAME_2, 1), (GAME_3, 2), (GAME_4, 3), (GAME_5, 4)])
def test_that_load_example_data_has_the_correct_entries(game, index):
    data = solution.load_data("example_data.txt")
    assert data[index] == game


@pytest.mark.parametrize("game, is_possible",
                         [(GAME_1, True), (GAME_2, True), (GAME_3, False), (GAME_4, False), (GAME_5, True)])
def test_that_if_a_game_is_possible_is_correctly_determined(game, is_possible):
    assert solution.is_possible(game, {'red': 12, 'green': 13, 'blue': 14}) is is_possible


def test_that_the_sum_of_possible_game_indices_is_correct_for_example_data():
    data = solution.load_data("example_data.txt")
    assert solution.get_result(data) == 8


@pytest.mark.parametrize("game, minimum_set", [
    (GAME_1, {'red': 4, 'green': 2, 'blue': 6}),
    (GAME_2, {'red': 1, 'green': 3, 'blue': 4}),
    (GAME_3, {'red': 20, 'green': 13, 'blue': 6}),
    (GAME_4, {'red': 14, 'green': 3, 'blue': 15}),
    (GAME_5, {'red': 6, 'green': 3, 'blue': 2}),
])
def test_that_the_minimum_set_is_correct_for_example_data(game, minimum_set):
    assert solution.minimum_set(game) == minimum_set


@pytest.mark.parametrize("game", [GAME_1, GAME_2, GAME_3, GAME_4, GAME_5])
def test_that_a_game_is_possible_given_its_minimum_set(game):
    assert solution.is_possible(game, solution.minimum_set(game))


@pytest.mark.parametrize("game, power", [(GAME_1, 48), (GAME_2, 12), (GAME_3, 1560), (GAME_4, 630), (GAME_5, 36)])
def test_that_power_of_set_is_correct_for_example(game, power):
    assert solution.power_of(solution.minimum_set(game)) == power


def test_that_the_sum_of_power_is_correct_for_example_data():
    data = solution.load_data("example_data.txt")
    assert solution.get_result_2(data) == 2286
