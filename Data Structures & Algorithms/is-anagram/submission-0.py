class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap = {}
        for c in s:
            if c in smap:
                smap[c] += 1
            else:
                smap[c] = 1
        
        tmap = {}
        for c in t:
            if c in tmap:
                tmap[c] += 1
            else:
                tmap[c] = 1
        
        for c in smap:
            if smap[c] != tmap.get(c, -1):
                return False


        return True