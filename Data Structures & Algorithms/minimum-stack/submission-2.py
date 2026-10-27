"""
My previous solution used a dictionary. Let's try again with two stacks.

We'll have:
    - Data stack, where we're putting the stuff to
    - Min stack, where we're keeping track of the minimum

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        # handle the base case
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minstack.append(val)
            return
        
        self.minstack.append(min(self.minstack[-1], val))
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
