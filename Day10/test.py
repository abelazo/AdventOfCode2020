import solution
import unittest


class TestClass(unittest.TestCase):

    def test_get_device_joltage(self):
        # GIVEN
        input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        input.sort()
        expected_joltage = input[-1] + 3

        # WHEN
        real_joltage = solution.get_device_joltage(input)

        # THEN
        self.assertEqual(expected_joltage, real_joltage)

    def test_get_valid_candidates(self):
        # GIVEN
        input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

        # WHEN
        valid_candidates = solution.get_valid_candidates(input, 4)

        # THEN
        self.assertEqual([5,6,7], valid_candidates)

    def test_get_differences_1(self):
        # GIVEN
        input = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]

        # WHEN
        ones, threes = solution.get_differences(input)

        # THEN
        self.assertEqual(7, len(ones))
        self.assertEqual(5, len(threes))

    def test_get_differences_longer(self):
        # GIVEN
        input = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
                 24, 23, 49, 45, 19, 38, 39, 11, 1, 32,
                 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

        # WHEN
        ones, threes = solution.get_differences(input)

        # THEN
        self.assertEqual(22, len(ones))
        self.assertEqual(10, len(threes))

    def test_solve_1(self):
        # GIVEN
        input = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
                 24, 23, 49, 45, 19, 38, 39, 11, 1, 32,
                 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

        # WHEN
        s = solution.solve_1(input)

        # THEN
        self.assertEqual(220, s)
        
        
if __name__ == '__main__':
    unittest.main()

