import solution


class TestPart1:
    def test_that_data_is_loaded(self):
        pass

    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result(data) == 0


class TestPart2:
    def test_that_result_is_correct_for_example(self):
        data = solution.load_data("example.txt")
        assert solution.get_result_2(data) == 0