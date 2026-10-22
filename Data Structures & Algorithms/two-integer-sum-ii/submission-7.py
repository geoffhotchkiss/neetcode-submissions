class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers is non-decreasing
        return values that are 1 indexed 

        goal: return [a, b] where numbers[a - 1] + numbers[b - 1] = target and a < b (-1 because 1 indexed)
        
        numbers = [1,2,3,4], target = 3

        [1,2,3,4]
         ^     ^  --> 5 > 3, so move left   
         ^   ^    --> 4 > 3, so move left
         ^ ^      --> 3 = 3, so done; 0,1 --> [1, 2]

        Why is this okay? I'm always adding the lowest possible number against the highest possible number. 
        
        If we're too big, then that larger number *is too big*:
            - I can't make the smaller number any smaller. 
            - All we can do is make the larger number smaller by moving left 

        If we're too small, then that smaller number *is too small*:
            - I can't make that larger number any larger. 
            - All can do is make the smaller number bigger by moving right  
        """
        a, b = 0, len(numbers)-1
        check = numbers[a] + numbers[b] 
        while check != target:
            if check > target:
                b -= 1
            else:
                a += 1
            check = numbers[a] + numbers[b] 

        return [a+1, b+1] 

