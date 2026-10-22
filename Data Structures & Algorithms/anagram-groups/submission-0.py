class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            stmp = ''.join(sorted(s))
            if anagrams.get(stmp):
                anagrams[stmp].append(s)
            else:
                anagrams[stmp] = [s]

        return list(anagrams.values())