class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 100:
            l = len(nums)
            for i in range(l):
                for j in range(i+1, min(l, i + indexDiff + 1)):
                    if i != j and nums[i] - nums[j] <= valueDiff and nums[j] - nums[i] <= valueDiff:
                        return True
            return False

        buckets = {}
        l = len(nums)
        for i in range(l):
            k = nums[i]
            if valueDiff != 0: k = int(nums[i] / valueDiff)
            if k in buckets.keys(): 
                buckets[k].add((i, nums[i]))
            else:
                buckets[k] = set()
                buckets[k].add((i, nums[i]))

        for i in range(l):
            k = nums[i]
            if valueDiff != 0: k = int(nums[i] / valueDiff)
            for t in buckets[k]:
                if i - t[0] <= indexDiff and t[0] - i <= indexDiff and i - t[0] != 0:
                    if nums[i] - t[1] <= valueDiff and t[1] - nums[i] <= valueDiff:
                        print(i, nums[i], t[0], t[1])
                        return True   
            if (k-1) in buckets.keys():
                for t in buckets[k-1]:
                    if i - t[0] <= indexDiff and t[0] - i <= indexDiff and i - t[0] != 0:
                        if nums[i] - t[1] <= valueDiff and t[1] - nums[i] <= valueDiff:
                            print(i, nums[i], t[0], t[1])
                            return True  
            if (k+1) in buckets.keys():
                for t in buckets[k+1]:
                    if i - t[0] <= indexDiff and t[0] - i <= indexDiff and i - t[0] != 0:
                        if nums[i] - t[1] <= valueDiff and t[1] - nums[i] <= valueDiff:
                            print(i, nums[i], t[0], t[1])
                            return True      

        return False
        