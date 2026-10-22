"""
[1,2,4,6]

0: 2*4*6
1: 1*4*6
2: 1*2*6
3: 1*2*4

>>> list(enumerate([1,2,4,6]))
[   (0, 1)  (1, 2)  (2, 4)  (3, 6)   ]

answer = [ 1  1  1  1  ]



"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        # more than one zero
        if nums.count(0) > 1:
            return [0]*len(nums)

        # Compute product of all
        # Compute product/nums[i] for each i 
        # Problem if there is one zero, then product is still 0 

        # if 1 zero
        if nums.count(0) == 1:
            answer = [0]*len(nums)
            product = 1
            for n in nums:
                if n != 0:
                    product *= n
            answer[nums.index(0)] = product 
            return answer

        # All non-zero: 
        product = 1
        for n in nums:
            product *= n
        
        answer = [product]*len(nums)
        for i,v in enumerate(nums):
            answer[i] = product//v
        return answer


