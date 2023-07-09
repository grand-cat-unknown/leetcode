from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_hashmap = {}
        for num in nums:
            if num not in nums_hashmap:
                nums_hashmap[num] = 1
            else:
                return True
        return False

# print(Solution().containsDuplicate(nums = [1, 2, 3, 1]))
