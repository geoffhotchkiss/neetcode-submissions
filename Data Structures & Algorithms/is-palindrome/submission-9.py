class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Create temp string t that is s but only alpha-numerics and all lower case
        """
        t = ""
        for c in s:
            if c.isalnum():
                t += c.lower()
        
        a,b = 0, len(t)-1

        while a <= b:
            if t[a] != t[b]:
                return False
            
            a += 1
            b -= 1
        
        return True
