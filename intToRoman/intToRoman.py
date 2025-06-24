class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        awnser = ""
        while True:
            if num >= 1000:
                num -= 1000
                awnser += "M"
            elif num >= 900:
                num -= 900
                awnser += "CM"
            elif num >= 500:
                num -= 500
                awnser += "D"
            elif num >= 400:
                num -= 400
                awnser += "CD"
            elif num >= 100:
                num -= 100
                awnser += "C"
            elif num >= 90:
                num -= 90
                awnser += "XC"
            elif num >= 50:
                num -= 50
                awnser += "L"
            elif num >= 40:
                num -= 40
                awnser += "XL"
            elif num >= 10:
                num -= 10
                awnser += "X"
            elif num >= 9:
                num -= 9
                awnser += "IX"
            elif num >= 5:
                num -= 5
                awnser += "V"
            elif num >= 4:
                num -= 4
                awnser += "IV"
            elif num >= 1:
                num -= 1
                awnser += "I"
            else:
                break
        return awnser