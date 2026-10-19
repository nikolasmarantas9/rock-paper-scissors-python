"""Unit tests for the Rock, Paper, Scissors game."""

import unittest

from rock_paper_scissors import determine_winner, CHOICES


class DetermineWinnerTests(unittest.TestCase):
    def test_same_move_is_draw(self):
        for move in CHOICES:
            with self.subTest(move=move):
                self.assertEqual(determine_winner(move, move), 0)

    def test_rock_beats_scissors(self):
        self.assertEqual(determine_winner(1, 3), 1)
        self.assertEqual(determine_winner(3, 1), 2)

    def test_paper_beats_rock(self):
        self.assertEqual(determine_winner(2, 1), 1)
        self.assertEqual(determine_winner(1, 2), 2)

    def test_scissors_beats_paper(self):
        self.assertEqual(determine_winner(3, 2), 1)
        self.assertEqual(determine_winner(2, 3), 2)


if __name__ == "__main__":
    unittest.main()
