'''
Find (i, j) in nums such that nums[i] + nums[j] == target

for each num[i]:
    goal_num = target - nums[i]
    does goal_num exist in nums? 
        yes: get index, and that's i,j 
        no: move on to i+1

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = nums[i]
            goal_num = target - a
            try:
                j = nums.index(goal_num, i+1)
                return [i,j]
            except ValueError:
                continue
        

