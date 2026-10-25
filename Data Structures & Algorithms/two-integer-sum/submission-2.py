class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Want the two indices where nums[i] + nums[j] == target, where i != j (i < j)

        So, if we have nums[i], does target - nums[j] exist in nums? Let's build a hashmap where 
        map[a] = index in nums of a. I wonder if it should be a list of indexs... 
        """

        indexes = {}

        for i,n in enumerate(nums):
            indexes[n] = indexes.get(n, []) + [i]

        for i,n in enumerate(nums):
            search = target-n

            if search in indexes:
                for j in indexes[search]:
                    if i == j:
                        continue
                    else:
                        return [i, j]


        