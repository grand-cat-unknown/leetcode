class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = []
        for str in strs:
            sorted_strs.append(''.join(sorted(str)))

        hm = {}
        for (x,y) in zip(strs,sorted_strs):
            if y in hm:
                hm[y].append(x)
            else:
                hm[y] = [x]

        only_values = [value for value in hm.values()]
        return (only_values)


print(Solution().groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))