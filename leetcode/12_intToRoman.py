class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""

        lookup = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"} # Slight increase in space requirements, but slightly more efficient time-wise

        while num != 0:
            numDigits = len(str(num))
            firstVal = int(str(num)[0])
            if firstVal<= 3:
                roman += lookup[1 * 10**(numDigits - 1)]
                num -= 1 * 10**(numDigits - 1)
            elif firstVal >= 5 and firstVal <= 8:
                roman += lookup[5 * 10**(numDigits - 1)]
                num -= 5 * 10**(numDigits - 1)
            else: # firstVal is 4 or 9
                roman += lookup[firstVal * 10**(numDigits - 1)]
                num -= firstVal * 10**(numDigits - 1)
        return roman

        