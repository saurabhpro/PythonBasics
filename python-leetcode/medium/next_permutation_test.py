import unittest

from next_permutation import next_perm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = next_perm([1, 2, 3])
        self.assertEqual(res, [1, 3, 2])

        res = next_perm([1, 3, 2])
        self.assertEqual(res, [2, 1, 3])

        res = next_perm([1, 3, 2, 7])
        self.assertEqual(res, [1, 3, 7, 2])

        res = next_perm([1, 3, 7, 2])
        self.assertEqual(res, [1, 7, 2, 3])

        res = next_perm([1, 7, 3, 2])
        self.assertEqual(res, [2, 1, 3, 7])

        res = next_perm([7, 3, 2, 1])
        self.assertEqual(res, [1, 2, 3, 7])


if __name__ == '__main__':
    unittest.main()
