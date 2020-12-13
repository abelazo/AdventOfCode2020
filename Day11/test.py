import unittest

import solution
from solution import Point

no_occupied_context = [Point.FLOOR, Point.FLOOR, Point.FLOOR,
                       Point.EMPTY,              Point.EMPTY,
                       Point.EMPTY, Point.EMPTY, Point.FLOOR]

three_occupied_context = [Point.OCCUPIED, Point.FLOOR, Point.FLOOR,
                          Point.OCCUPIED,              Point.EMPTY,
                          Point.OCCUPIED, Point.FLOOR, Point.FLOOR]

four_occupied_context = [Point.OCCUPIED, Point.FLOOR, Point.OCCUPIED,
                         Point.OCCUPIED,              Point.EMPTY,
                         Point.OCCUPIED, Point.FLOOR, Point.FLOOR]

example = ["L.LL.LL.LL",
           "LLLLLLL.LL",
           "L.L.L..L..",
           "LLLL.LL.LL",
           "L.LL.LL.LL",
           "L.LLLLL.LL",
           "..L.L.....",
           "LLLLLLLLLL",
           "L.LLLLLL.L",
           "L.LLLLL.LL"]

class TestClass(unittest.TestCase):

    def test_get_status(self):
        # GIVEN
        context = [Point(1, x, '.') for x in range(8)]
        expected_status = Point.EMPTY
        p = Point(1, 2, expected_status)
        p.set_context(context)

        # WHEN
        status = p.get_status()

        # THEN
        self.assertEqual(status, expected_status)

    def test_floor_should_never_switch(self):
        # GIVEN
        context = [Point(1, x, '.') for x in range(8)]
        p = Point(1, 2, Point.FLOOR)
        p.set_context(context)

        # WHEN
        status = p.new_status()

        # THEN
        self.assertEqual(status, Point.FLOOR)

    def test_empty_should_switch_to_occupied(self):
        # GIVEN
        context = [Point(1, 1, x) for x in no_occupied_context]
        p = Point(1, 2, Point.EMPTY)
        p.set_context(context)

        # WHEN
        status = p.new_status()

        # THEN
        self.assertEqual(status, Point.OCCUPIED)

    def test_empty_should_not_switch_to_occupied(self):
        # GIVEN
        context = [Point(1, 1, x) for x in three_occupied_context]
        p = Point(1, 2, Point.EMPTY)
        p.set_context(context)

        # WHEN
        status = p.new_status()

        # THEN
        self.assertEqual(status, Point.EMPTY)
        
    def test_occupied_should_switch_to_empty(self):
        # GIVEN
        context = [Point(1, 1, x) for x in four_occupied_context]
        p = Point(1, 2, Point.OCCUPIED)
        p.set_context(context)

        # WHEN
        status = p.new_status()

        # THEN
        self.assertEqual(status, Point.EMPTY)

    def test_occupied_should_not_switch_to_empty(self):
        # GIVEN
        context = [Point(1, 1, x) for x in three_occupied_context]
        p = Point(1, 2, Point.OCCUPIED)
        p.set_context(context)

        # WHEN
        status = p.new_status()

        # THEN
        self.assertEqual(status, Point.OCCUPIED)


    def test_generate_points(self):
        # GIVEN

        # WHEN
        points = solution.generate_points(example)

        # THEN
        for r in range(len(example)):
            for c in range(len(example[r])):
                points[r][c].get_status() == example[r][c]

    def test_get_context(self):
        # GIVEN
        points = solution.generate_points(example)

        # WHEN
        context = solution.get_context(points, 1, 1)

        # THEN
        expected_context = [Point.EMPTY, Point.FLOOR, Point.EMPTY, Point.EMPTY, Point.EMPTY, Point.EMPTY, Point.FLOOR, Point.EMPTY]
        for i in range(len(context)):
            self.assertEqual(context[i].get_status(), expected_context[i])

    def test_get_upper_limit_context(self):
        # GIVEN
        points = solution.generate_points(example)

        # WHEN
        context = solution.get_context(points, 0, 0)

        # THEN
        expected_context = [Point.FLOOR, Point.EMPTY, Point.EMPTY]
        for i in range(len(context)):
            self.assertEqual(context[i].get_status(), expected_context[i])


    def test_get_lower_limit_context(self):
        # GIVEN
        points = solution.generate_points(example)

        # WHEN
        context = solution.get_context(points, 9, 9)

        # THEN
        expected_context = [Point.FLOOR, Point.EMPTY, Point.EMPTY]
        for i in range(len(context)):
            self.assertEqual(context[i].get_status(), expected_context[i])


    def test_solution1(self):
        # GIVEN
        points = solution.generate_points(example)

        # WHEN
        seats = solution.solve_1(points)

        # THEN
        self.assertEqual(seats, 37)

if __name__ == '__main__':
    unittest.main()

