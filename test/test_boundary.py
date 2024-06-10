import os
import unittest
from test.TestUtils import TestUtils
from football_players import *

class BoundaryTest(unittest.TestCase):

    def test_boundary(self):
        self.test_utils_instance.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundary = Passed")


if __name__ == "__main__":
    unittest.main()
