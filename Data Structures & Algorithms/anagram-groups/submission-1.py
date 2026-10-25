class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        hashmap: key = hashmap of c's + counts, val is the list of words with that 
        """

        def word_hash(s: str) -> str: 
            cache = {}
            for c in s:
                cache[c] = cache.get(c, 0) + 1
                # (a, 1) (b, 1) (c, 1) = cab, abc 

            result = ""
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c in cache:
                    result += str(cache[c]) + c
            
            return result

        # anagram map, key = word_map(word), value list of words with that same wordmap 
        amap = {}

        for word in strs:
            wh = word_hash(word)
            amap[wh] = amap.get(wh, []) + [word]

        result = []
        for wh in amap:
            result.append(amap[wh])

        return result