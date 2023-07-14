class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if (num - 1) not in num_set:
                curr_num = num
                curr_len = 1
                while curr_num + 1 in num_set:
                    curr_len += 1
                    curr_num += 1
                max_len = max(curr_len, max_len)

        return max_len


# print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))