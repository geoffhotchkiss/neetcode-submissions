class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A palindrome is a string that reads the same forward and backward. 
        It is also case-insensitive and ignores all non-alphanumeric characters.
        So let's transform s into lower case with all non-alphanumeric chars removed 

        s="Was it a car or a cat I saw?"
        """

        check = ""
        for c in s:
            if c.isalnum():
                check += c.lower()
        
        print(f"{check=}")

        left = 0
        right = len(check) - 1

        while left <= right:
            if check[left] != check[right]:
                return False
            left += 1
            right -= 1

        return True


