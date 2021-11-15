from typing import List


class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for num in nums:
            if num in hashset:
                return True
            hashset[num] = True

        return False
