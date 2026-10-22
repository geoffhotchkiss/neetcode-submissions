class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        ddnums = set(nums)
        longest = 1

        for n in ddnums:
            if n - 1 in ddnums:
                # skip n's for which n-1 exists as those will be counted later
                continue
            
            count = 1
            check = n+1
            while check in ddnums:
                count += 1
                check += 1
            if count > longest:
                longest = count

        return longest
            
