class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1: return 5
        oldVals = [1,1,1,1,1]

        for i in range(n - 1):
            newVals = [0,0,0,0,0]
            newVals[0] = oldVals[1] + oldVals[2] + oldVals[4]
            newVals[1] = oldVals[0] + oldVals[2]
            newVals[2] = oldVals[1] + oldVals[3]
            newVals[3] = oldVals[2]
            newVals[4] = oldVals[2] + oldVals[3]

            for j in range(5):
                oldVals[j] = newVals[j]
        count = sum(oldVals)
        return count % 1000000007
        