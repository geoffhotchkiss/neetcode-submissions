class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            a, b = s[i], s[len(s)-i-1]
            s[i] = b
            s[len(s)-i-1] = a

         