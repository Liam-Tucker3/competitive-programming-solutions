class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        count = 1
        if len(self.prices) == 0:
            self.prices.append( (price, count))
            return count
        while len(self.prices) > 0 and price >= self.prices[-1][0]: # Price is at least as good as last relevant day
            count += self.prices[-1][1]
            self.prices = self.prices[:-1]
        self.prices.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)