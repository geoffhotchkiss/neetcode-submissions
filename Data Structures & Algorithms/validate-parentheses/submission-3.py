class Solution:
    def isValid(self, s: str) -> bool:
        """
        Valid when:
            - every open has a close
            - brackets are opened/closed in the correct order
            - every close has an open

        Strat: 
            - loop through s and check if each c is a paren
            - if it's an open, add it to a stack
            - if it's a close, pop off the top of that stack and check if it matches
            - if it matches, we're good (the open has a close)
            - if it doesn't match, it's invalid (the order is wrong)
            - at end, expect that stack to be empty (every close is opened)

        Need to consider if the stack if empty when we try to pop something off
        """

        open_parens  = set([ "{", "(", "[" ])
        close_parens = set([ "}", ")", "]" ])

        opens = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        cache = []

        for c in s:
            if c in open_parens:
                cache.append(c)
            
            if c in close_parens:
                # We're trying to close a paren, but there are no more opens
                if len(cache) == 0:
                    return False

                # We have an out of order close, we can only close the most recent open
                if cache.pop() != opens[c]:
                    return False
        
        return len(cache) == 0
                

                


        