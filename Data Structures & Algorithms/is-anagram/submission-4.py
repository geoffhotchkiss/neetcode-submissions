class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        """
        Count up the chars in s and store in seen, so seen[c] == number of times c was in s

        Then loop through c in t, and decrement each seen[c]. 

        If c is not in seen, false. 

        At the end, if any seen[c] is > 0, false
        """
        seen = {} 
        for c in s:
            seen[c] = seen.get(c, 0) + 1

        for c in t:
            if c not in seen:
                return False

            seen[c] = seen[c] - 1

        for c in seen:
            if seen[c] > 0:
                return False

        return True