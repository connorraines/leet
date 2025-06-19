def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    x_str = str(x)
    if x < 0:
        reversed_str = '-'
        reversed_str += x_str[:0:-1]
    else:
        reversed_str = x_str[::-1]
    reversed_int = int(reversed_str)
    if reversed_int < -2**31 or reversed_int > 2**31 - 1:
        return 0
    return reversed_int
        