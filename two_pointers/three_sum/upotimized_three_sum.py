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
            num_copy[idx] = 12345678910
            two_sum_idxs = list(self.twoSum(num_copy, -i))
            # print("i: ", i)
            # print("with: ", nums)
            # print("without: ", num_copy)
            # print("target: ", -i)
            # print(two_sum_idxs)
            for one in two_sum_idxs:
                # print("answers: ", nums[one[0]], nums[one[1]], i)
                result.add(tuple( sorted([nums[one[0]], nums[one[1]], i])))
            # print("-------")

        return result


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for idx, val in enumerate(nums):
            if val in hashmap:
                hashmap[val]['val'].append(idx)
            else:
                hashmap[val] = {}
                hashmap[val]['val'] = [idx]

        subtracted_nums = [(target - x) for x in nums]

        for idx, val in enumerate(subtracted_nums):
            if val in hashmap:
                if 'sub_val' in hashmap[val]:
                    hashmap[val]['sub_val'].append(idx)
                else:
                    hashmap[val]['sub_val'] = [idx]

        result = set()
        for key in hashmap:
            # print(hashmap[key])
            if len(hashmap[key]['val']) > 0 and 'sub_val' in hashmap[key] and len(hashmap[key]['sub_val']) > 0:
                all_possible_pairs = set()
                for i in hashmap[key]['val']:
                    for j in hashmap[key]['sub_val']:
                        if i != j:
                            all_possible_pairs.add(tuple(sorted([i, j])))
                result = result.union(all_possible_pairs)
        return result

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
