import pytest
import solution
import numpy as np


class TestPart1:
    def test_load_data_returns_maze(self):
        maze = solution.load_data("example_1.txt")
        assert maze._tiles.shape == (5, 5)

    @pytest.mark.parametrize("filename, x, y", [("example_1.txt", 1, 1), ("example_2.txt", 0, 2)])
    def test_that_start_position_is_found(self, filename, x, y):
        maze = solution.load_data(filename)
        assert maze._current_x == x
        assert maze._current_y == y

    @pytest.mark.parametrize("filename, result", [("example_1.txt", 4), ("example_2.txt", 8)])
    def test_that_result_is_correct_for_example_data(self, filename, result):
        maze = solution.load_data(filename)
        assert solution.get_result(maze) == result


class TestPart2:
    @pytest.mark.parametrize("filename, result", [
        ("example_1.txt", 1),
        ("example_2.txt", 1),
        ("example_3.txt", 4),
        ("example_4.txt", 8),
        ("example_5.txt", 10)
    ])
    def test_that_result_is_correct_for_example_data(self, filename, result):
        maze = solution.load_data(filename)
        assert solution.get_result_2(maze) == result

    def test_that_main_loop_tiles_is_free_of_junk_pipes(self):
        maze_with_junk = solution.load_data("example_3_with_junk.txt")
        maze = solution.load_data("example_3.txt")
        assert np.all(maze_with_junk._main_loop_tiles == maze._tiles)

    @pytest.mark.parametrize("filename, start_tile", [
        ("example_1.txt", "F"),
        ("example_2.txt", "F"),
        ("example_3.txt", "F"),
        ("example_4.txt", "F"),
        ("example_5.txt", "7")
    ])
    def test_that_start_tile_is_identified(self, filename, start_tile):
        maze = solution.load_data(filename)
        assert maze._identify_start_tile() == start_tile

    def test_that_sides_are_marked_on_main_loop_tiles(self):
        maze = solution.load_data("example_1.txt")
        maze_marked = solution.load_data("example_1_marked.txt")
        assert np.all(maze._inner_outer_tiles == maze_marked._main_loop_tiles)
