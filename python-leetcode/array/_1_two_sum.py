# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List


def two_sum_indexes(nums: List[int], target: int) -> List[int]:
    dictionary = {}

    for i in range(len(nums)):
        second_number = target - nums[i]
        if second_number in dictionary.keys():
            second_index = nums.index(second_number)

            return sorted([i, second_index])

        dictionary.update({nums[i]: i})


def two_sum_values(nums: List[int], target: int) -> List[int]:
    nums.sort()
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return [nums[i], nums[j]]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1


def twoSum(nums: List[int], target: int) -> List[int]:
    dictionary = {}

    for index, value in enumerate(nums):
        dictionary[value] = index

    print(dictionary)
    for i in range(len(nums)):
        second_number = target - nums[i]
        if second_number in dictionary.keys():
            second_index = nums.index(second_number)

            if i != second_index:
                return sorted([i, second_index])
