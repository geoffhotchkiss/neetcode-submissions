class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0

        count_ones = 0
        for n in nums:
            if n == 1:
                count_ones += 1
                curr_max = max(count_ones, curr_max)
            else:
                count_ones = 0

        return curr_max