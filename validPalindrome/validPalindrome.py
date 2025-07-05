class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Preprocess the string: remove non-alphanumeric characters and convert to lowercase
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        # Check if the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]