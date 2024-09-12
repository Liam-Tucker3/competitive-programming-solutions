class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        vals = []
        for b in boxTypes:
            vals.append( (b[1], b[0]))
        vals = list(reversed(sorted(vals)))
        count = 0
        while truckSize > 0:
            if vals[0][1] >= truckSize:
                count += truckSize * vals[0][0]
                return count
            count += vals[0][0] * vals[0][1]
            truckSize -= vals[0][1]
            vals = vals[1:]
            if len(vals) == 0: break
        return count

        