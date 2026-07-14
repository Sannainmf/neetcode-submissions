class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):

        self.left = ListNode(-1, None, None)
        self.hp = ListNode(homepage, None, self.left)
        self.right = ListNode(-1, None, self.hp)
        self.hp.next = self.right
        self.left.next = self.hp

        self.curr = self.hp

    def visit(self, url: str) -> None:

        end = self.right
        self.curr.next = end
        end.prev = self.curr

        newLink = ListNode(url, None, None)
        self.curr.next = newLink
        end.prev = newLink
        newLink.prev = self.curr
        newLink.next = end

        self.curr = self.curr.next

    def back(self, steps: int) -> str:

        while self.curr.val != -1 and steps > 0:
            self.curr = self.curr.prev
            steps -= 1

        if self.curr.val == -1:
            steps -= 1
            t = self.curr.next.val
            self.curr = self.curr.next
            return t
        else:
            return self.curr.val
            
    def forward(self, steps: int) -> str:

        while self.curr.val != -1 and steps > 0:
            self.curr = self.curr.next
            steps -= 1

        if self.curr.val == -1:
            steps -= 1
            t = self.curr.prev.val
            self.curr = self.curr.prev
            return t
        else:
            return self.curr.val


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)