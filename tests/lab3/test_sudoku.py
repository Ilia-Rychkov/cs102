import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src" / "lab3"))

import unittest

from sudoku import group, get_row, get_col, get_block, find_empty_positions, find_possible_values, solve, check_solution, generate_sudoku



class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(
            group([1, 2, 3, 4], 2),
            [[1, 2], [3, 4]]
        )

        self.assertEqual(
            group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        )
    def test_get_row(self):
        grid = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        self.assertEqual(get_row(grid, (1, 0)), ["4", "5", "6"])

    def test_get_col(self):
        grid = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        self.assertEqual(get_col(grid, (0, 1)), ["2", "5", "8"])
    def test_get_block(self):
        grid = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
            ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
            ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
            ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
            ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
            ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
            ["9", "1", "2", "3", "4", "5", "6", "7", "8"]
        ]

        self.assertEqual(
            get_block(grid, (0, 0)),
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        )

        self.assertEqual(
            get_block(grid, (4, 4)),
            ["5", "6", "7", "8", "9", "1", "2", "3", "4"]
        )
    def test_find_empty_positions(self):
        grid = [
            ["1", "2", "."],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        self.assertEqual(find_empty_positions(grid), (0, 2))
    def test_find_empty_positions_full(self):
        grid = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        self.assertIsNone(find_empty_positions(grid))
    def test_find_possible_values(self):
        grid = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

        self.assertEqual(
            find_possible_values(grid, (0, 2)),
            {"1", "2", "4"}
        )

        self.assertEqual(
            find_possible_values(grid, (4, 7)),
            {"2", "5", "9"}
        )
    def test_solve(self):
        grid = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

        solution = solve(grid)

        self.assertIsNotNone(solution)
        self.assertEqual(solution[0], ["5", "3", "4", "6", "7", "8", "9", "1", "2"])
        self.assertEqual(
            sum(row.count(".") for row in solution),
            0
        )
    def test_check_solution_correct(self):
        grid = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

        solution = solve(grid)

        self.assertTrue(check_solution(solution))

    def test_check_solution_wrong(self):
        grid = [
            ["1", "1", "3", "4", "5", "6", "7", "8", "9"]
        ] * 9

        self.assertFalse(check_solution(grid))
    def test_generate_sudoku(self):
        grid = generate_sudoku(40)

        filled = sum(row.count(".") for row in grid)

        self.assertEqual(filled, 41)

        solution = solve(grid)
        self.assertTrue(check_solution(solution))

    def test_generate_sudoku_full(self):
        grid = generate_sudoku(1000)

        empty = sum(row.count(".") for row in grid)

        self.assertEqual(empty, 0)
        self.assertTrue(check_solution(grid))

    def test_generate_sudoku_empty(self):
        grid = generate_sudoku(0)

        empty = sum(row.count(".") for row in grid)

        self.assertEqual(empty, 81)
if __name__ == "__main__":
    unittest.main()