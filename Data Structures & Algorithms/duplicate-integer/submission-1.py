class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for num in nums:
            if num in dups:
                return True
            else:
                dups[num] = 0
        return False
