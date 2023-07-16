from copy import copy


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # print(nums)

        nums = self.preprocess(nums)

        # print(nums)
        result = set()
        for idx, i in enumerate(nums):
            num_copy = copy(nums)
            two_sum_idxs = list(self.twoSum(num_copy, -i, idx))
            for one in two_sum_idxs:
                # print("answers: ", nums[one[0]], nums[one[1]], i)
                result.add(tuple( sorted([nums[one[0]], nums[one[1]], i])))
            # print("-------")

        return result


    def twoSum(self, nums, target, skip_idx):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for idx, val in enumerate(nums):
            if idx == skip_idx:
                continue
            if val in hashmap:
                hashmap[val].append(idx)
            else:
                hashmap[val] = {}
                hashmap[val] = [idx]

            if (target - val) in hashmap and hashmap[(target - val)][0] != idx:
                yield (idx, hashmap[target-val][0])

    def addToHashmap(self, array, hashmap):
        for idx, num in enumerate(array):
            if num in hashmap:
                hashmap[num].append(idx)
            else:
                hashmap[num] = [idx]
        return hashmap

    def sumOfValuesAtIndices(self, set, nums):
        sum = 0
        for idx in set:
            sum += nums[idx]
        return sum

    def preprocess(self, nums):
        hashmap = {}
        for i in nums:
            if i in hashmap:
                if len(hashmap[i]) <= 3:
                    hashmap[i].append(i)
            else:
                hashmap[i] = [i]

        # print(hashmap)
        result = []
        for i in hashmap:
            result = result + hashmap[i]

        return result

# print(Solution()
#       .threeSum(nums = [-1,0,1,2,-1,-4]))
