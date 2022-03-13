# -*- coding: utf-8 -*-

from .context import src
from src import core

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertEqual(core.add_one(1), 2)


if __name__ == '__main__':
    unittest.main()
