class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_str_reversed = x_str[::-1]
        if x_str == x_str_reversed:
            return True
        else:
            return False