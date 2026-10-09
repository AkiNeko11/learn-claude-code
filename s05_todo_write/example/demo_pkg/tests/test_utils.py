"""Tests for demo_pkg.utils."""

import unittest

from demo_pkg.utils import add, multiply


class TestUtils(unittest.TestCase):
    """Tests for the utility functions."""

    def test_add(self) -> None:
        """Test that add returns the sum of two numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self) -> None:
        """Test that multiply returns the product of two numbers."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 4), -8)


if __name__ == "__main__":
    unittest.main()
