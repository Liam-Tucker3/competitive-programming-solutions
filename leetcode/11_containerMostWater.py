class Solution:
    def maxArea(self, height: List[int]) -> int:
        lower = 0
        upper = len(height) - 1

        maxSize = (upper - lower) * min(height[lower], height[upper])

        while upper > lower:
            if height[lower] < height[upper]:
                lower += 1
            else:
                upper -= 1
            
            newSize = (upper - lower) * min(height[lower], height[upper])
            # print(lower, upper, newSize)
            maxSize = max(newSize, maxSize)
        
        return maxSize
        