class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_digits = ''.join(str(digit) for digit in digits)
        incremented_value = int(str_digits) + 1
        return [int(digit) for digit in str(incremented_value)]