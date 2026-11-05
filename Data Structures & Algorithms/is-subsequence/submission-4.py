class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        from collections import deque
        check_stack = deque(s)
        
        if len(t) == 0 and len(s) == 0:
            return True

        if len(s) == 0:
            return True

        if len(t) == 0 and len(s) > 0:
            return False

        
        check_char = check_stack.popleft()
        for c in t:
            if c == check_char:
                if len(check_stack) == 0:
                    return True
                check_char = check_stack.popleft()

        return False

        