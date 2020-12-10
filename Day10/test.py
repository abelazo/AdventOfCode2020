import solution
import unittest

_short_input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
_long_input = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
               24, 23, 49, 45, 19, 38, 39, 11, 1, 32,
               25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]


class TestClass(unittest.TestCase):

    def test_get_device_joltage(self):
        # GIVEN
        input = _short_input.copy()
        input.sort()
        expected_joltage = input[-1] + 3

        # WHEN
        real_joltage = solution.get_device_joltage(_short_input)

        # THEN
        self.assertEqual(expected_joltage, real_joltage)

    def test_get_valid_candidates(self):
        # GIVEN
        input = _short_input.copy()

        # WHEN
        valid_candidates = solution.get_valid_candidates(input, 4)

        # THEN
        self.assertEqual([5,6,7], valid_candidates)

    def test_get_differences_1(self):
        # GIVEN
        input = _short_input.copy()

        # WHEN
        ones, threes = solution.get_differences(input)

        # THEN
        self.assertEqual(7, len(ones))
        self.assertEqual(5, len(threes))

    def test_get_differences_longer(self):
        # GIVEN
        input = _long_input.copy()

        # WHEN
        ones, threes = solution.get_differences(input)

        # THEN
        self.assertEqual(22, len(ones))
        self.assertEqual(10, len(threes))

    def test_solve_1(self):
        # GIVEN
        input = _long_input.copy()

        # WHEN
        s = solution.solve_1(input)

        # THEN
        self.assertEqual(220, s)

    def test_solve_2_short(self):
        # GIVEN
        input = _short_input.copy()

        # WHEN
        s = solution.solve_2(input)

        # THEN
        self.assertEqual(8, s)

    @unittest.skip("For debugging")
    def test_solve_2_long(self):
        # GIVEN
        input = _long_input.copy()

        # WHEN
        s = solution.solve_2(input)

        # THEN
        self.assertEqual(19208, s)
        
        
if __name__ == '__main__':
    unittest.main()

