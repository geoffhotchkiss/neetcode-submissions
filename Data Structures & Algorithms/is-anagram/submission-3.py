'''
anagrams:
    racecar
    carrace

same chars, just different order
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)