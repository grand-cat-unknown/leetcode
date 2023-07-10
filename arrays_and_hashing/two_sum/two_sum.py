class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_set = self.addToHashmap(nums, {})
        subtracted_nums = [(target - x) for x in nums]
        hash_set = self.addToHashmap(subtracted_nums,hash_set)

        for key in hash_set:
            # print(hash_set[key])
            if len(hash_set[key]) == 2:
                if self.sumOfValuesAtIndices(hash_set[key],nums) == target:
                    return hash_set[key]

    def addToHashmap(self, array, hashmap):
        for idx, num in enumerate(array):
            if num in hashmap:
                hashmap[num].add(idx)
            else:
                hashmap[num] = {idx}
        return hashmap

    def sumOfValuesAtIndices(self, set, nums):
        sum = 0
        for idx in set:
            sum += nums[idx]
        return sum