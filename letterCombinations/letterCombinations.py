class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        result = ['']
        for digit in digits:
            if digit not in letters:
                continue
            new_result = []
            for combination in result:
                for letter in letters[digit]:
                    new_result.append(combination + letter)
            result = new_result
        return result