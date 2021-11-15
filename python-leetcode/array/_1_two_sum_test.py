# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


import unittest

from _1_two_sum import two_sum_values, two_sum_indexes, twoSum


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = two_sum_indexes([2, 7, 11, 15], 9)
        self.assertEqual([0, 1], res)

        res = two_sum_indexes([3, 2, 4], 6)
        self.assertEqual([1, 2], res)

        res = two_sum_values([3, 2, 4], 6)
        self.assertEqual([2, 4], res)

        res = twoSum([3, 2, 4], 6)
        self.assertEqual([1, 2], res)


if __name__ == '__main__':
    unittest.main()
