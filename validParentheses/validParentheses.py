class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        answer = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pairs.values():
                answer.append(char)
            elif char in pairs.keys():
                if not answer or answer[-1] != pairs[char]:
                    return False
                answer.pop()
        return not answer