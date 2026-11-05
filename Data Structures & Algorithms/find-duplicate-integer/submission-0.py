class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        dup = c.most_common(1)
        return dup[0][0]