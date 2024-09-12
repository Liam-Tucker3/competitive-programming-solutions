class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

        val = 0
        i = 0
        while i < len(s):
            if i+1 == len(s): # Case where this is the last digit left
                val += lookup[s[i]]
                break
            elif s[i:i+2] in lookup:
                val += lookup[s[i:i+2]]
                i += 2
            else:
                val += lookup[s[i:i+1]]
                i += 1
        return val
        