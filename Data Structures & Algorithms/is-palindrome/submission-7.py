class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
            0123456
            tacocat 
            ^     ^
            0-6
            1-5
            2-4
            3-4
            "Was it a car or a cat I saw?"
            w-? 
            w-w
            a-a
            s-s 
            _-_
            i-i
            t-_
            t-t
        """
        a, b = 0, len(s)-1

        while a <= b:
            while not s[a].isalnum():
                a += 1
                if a >= len(s):
                    return True
            
            while not s[b].isalnum():
                b -= 1
                if b < 0:
                    return True

            print(f"{a=},{b=}")
            if s[a].lower() != s[b].lower():
                return False

            a += 1
            b -= 1
        
        return True
        