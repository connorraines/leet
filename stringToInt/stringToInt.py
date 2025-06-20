class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        has_negative_sign = False
        s_list = list(s.strip())
        new_s = []
        if len(s_list) == 0:
            return 0
        if s_list[0] == '-' :
            has_negative_sign = True
            s_list.pop(0)
        elif s_list[0] == '+':
            s_list.pop(0)
        for char in s_list:
            if char in '0123456789':
                new_s.append(char)
            else:
                break
        if len(new_s) == 0:
            return 0
        new_s = ''.join(new_s)
        new_s = int(new_s)
        if has_negative_sign:
            new_s = -new_s
        if new_s < -2**31:
            return -2**31
        elif new_s > 2**31 - 1:
            return 2**31 - 1
        return new_s
        
