class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        for idx, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = [idx]
            else:
                hashmap[num].append(idx)

        return_array = []
        for _ in range(k):
            max_len = 0
            max_number = -1
            for x in hashmap:
                if max_len < len(hashmap[x]):
                    max_len = len(hashmap[x])
                    max_number = x

            return_array.append(max_number)
            hashmap[max_number] = []

        return return_array




# print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k=3))