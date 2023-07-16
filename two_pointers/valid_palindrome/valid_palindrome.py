class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stripped_s = ''.join(alphanum.lower() for alphanum in s if alphanum.isalnum())
        return stripped_s == stripped_s[::-1]


# print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
