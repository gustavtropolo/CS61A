from discussion5_trees import tree, Path, is_tree, is_leaf
import unittest

class HasPath(unittest.TestCase):
    def setUp(self):
        self.solution = Path()

    def testBasic(self):
        t2 = tree(5, [tree(6), tree(7)]) # -> [5, [6], [7]]
        t1 = tree(3, [tree(4), t2])
        self.assertTrue(self.solution.has_path(t2, [5, 6]))

    def test2(self):
        self.assertEqual(True, True)