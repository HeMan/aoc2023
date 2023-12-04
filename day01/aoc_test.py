import unittest

import aoc


class TestAoc(unittest.TestCase):
    def test_get_solution_1_should_return_sum_of_input_entries(self):
        self.assertEqual(
            aoc.get_solution_part1(
                ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
            ),
            142,
        )

    def test_get_solution_2_should_return_product_of_input_entries(self):
        self.assertEqual(
            aoc.get_solution_part2(
                [
                    "two1nine",
                    "eightwothree",
                    "abcone2threexyz",
                    "xtwone3four",
                    "4nineeightseven2",
                    "zoneight234",
                    "7pqrstsixteen",
                ]
            ),
            281,
        )


if __name__ == "__main__":
    unittest.main()
