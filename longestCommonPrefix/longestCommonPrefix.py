class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s):
                    return strs[0][:i]
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


