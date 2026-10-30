"""
Each row is sorted in non-decreasing order.
The first num in each row is larger than the last in the previous. 

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Let's try to take advantage of the sortedness. The long term goal is to bsearch to find the row, then bsearch within the row to find the element. 

        First, we check to see if the target is within the range of each row. Then we'll bsearch that row for target. 
        """
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return target in row

        return False