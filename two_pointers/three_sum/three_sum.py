class Solution(object):
    def threeSum(self, nums):
        nums = self.preprocess(nums)
        result = set()
        for idx, i in enumerate(nums):
            for one in self.twoSum(nums, -i, idx):  # Directly iterate over the generator
                result.add(tuple(sorted([nums[one[0]], nums[one[1]], i])))
        return result

    def twoSum(self, nums, target, skip_idx):
        hashmap = {}
        for idx, val in enumerate(nums):
            if idx == skip_idx:  # Skip the element that is currently being used in threeSum
                continue
            if val in hashmap:
                hashmap[val].append(idx)
            else:
                hashmap[val] = [idx]
            sub_val = target - val
            if sub_val in hashmap and hashmap[sub_val][0] != idx:  # Check if the complement is already in the hashmap and it's not the same element
                yield (hashmap[sub_val][0], idx)

    def preprocess(self, nums):
        hashmap = {}
        for i in nums:
            if i in hashmap:
                if hashmap[i] < 3:
                    hashmap[i] += 1
            else:
                hashmap[i] = 1

        result = []
        for num, count in hashmap.items():
            result.extend([num] * min(count, 3))  # Limit the number occurrence to 3

        return result
