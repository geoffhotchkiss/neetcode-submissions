class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We have n. Does k=target-n exist in the list? 
        We know numbers is non-decreasing. So it could look like [0, 1, 2, 4, 5, 6].
        So we will always search foward. So if k is ever 
        """

        i = 0
        j = len(numbers) - 1

        done = False
        while not done:
            a, b = numbers[i], numbers[j]

            if a + b == target:
                return [i+1, j+1]
            
            if a + b > target:
                j -= 1

            if a + b < target:
                i += 1



        
            
