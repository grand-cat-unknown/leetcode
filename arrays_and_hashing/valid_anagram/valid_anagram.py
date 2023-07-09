class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}

        for one in s:
            if one in s_hash:
                s_hash[one] = s_hash[one] + 1
            else:
                s_hash[one] = 1

        for one_t in t:
            if one_t in s_hash:
                s_hash[one_t] = s_hash[one_t] - 1
            else:
                return False

        for remaining in s_hash:
            if s_hash[remaining] != 0:
                return False

        return True


# print(Solution().isAnagram(s = "anagram", t = "nagaram"))