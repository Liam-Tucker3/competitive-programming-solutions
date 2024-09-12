class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = [0 for i in range(len(l))]
        for i in range(len(l)):
            low = l[i]
            high = r[i]
            if (high - low) < 2:
                output[i] = True
                continue
            vals = nums[low:high+1]
            vals = sorted(vals)
            # print(i, vals)
            diff = vals[1] - vals[0]
            failCase = False
            for j in range(1, len(vals) - 1):
                # print(j, vals[j], vals[j+1])
                if vals[j+1] - vals[j] != diff:
                    output[i] = False
                    failCase = True
                    break
            if not failCase:
                output[i] = True
        return output
            
            
        