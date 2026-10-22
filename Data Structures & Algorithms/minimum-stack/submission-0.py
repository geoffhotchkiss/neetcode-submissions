class MinStack:

    def __init__(self):
        self.stack = []
        self.cache = {} # mapping length of stack to min at that length

    def push(self, val: int) -> None:
        self.stack.append(val)
        size = len(self.stack)

        if size == 1:
            self.cache[size] = val
        else:
            # check prev min, and check if val is smaller than it
            self.cache[size] = min(self.cache[size-1], val)

    def pop(self) -> None:
        size = len(self.stack)
        del( self.cache[size] )
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.cache[len(self.stack)]
