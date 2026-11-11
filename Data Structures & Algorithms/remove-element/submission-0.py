class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = 0

        import math

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[answer] = nums[i]
                answer += 1
        return answer