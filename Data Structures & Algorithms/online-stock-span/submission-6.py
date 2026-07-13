class StockSpanner:

    def __init__(self):

        self.stack = []
        

    def next(self, price: int) -> int:

        counter = 1
        
        if not self.stack:
            self.stack.append(price)
        else:
            while counter <= len(self.stack) and self.stack[-counter] <= price:
                counter += 1

            self.stack.append(price)

        return counter
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)