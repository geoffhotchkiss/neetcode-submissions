class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Start from the left and move right. Keep track of chars in a set (to test for dupes) and length. 
        
        If we hit something in the set, our best shot of getting a longer string is to shift the left side and remove the left value from the set. 
        """

        max_length = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            c = s[right]

            while c in seen:
                # remove the left side, advance left, check again
                seen.remove(s[left])
                left += 1

            seen.add(c)
            
            max_length = max(max_length, right - left + 1)

        return max_length

