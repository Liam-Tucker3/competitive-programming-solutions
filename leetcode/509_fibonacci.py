class Solution:
    def fib(self, n: int) -> int:
        # Edge Cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Main Approach
        vals = [0 for i in range(n + 1)]
        vals[1] = 1
        for i in range(2, n + 1):
            vals[i] = vals[i - 1] + vals[i - 2]
        return vals[-1]
