"""
Each row is sorted in non-decreasing order.
The first num in each row is larger than the last in the previous. 

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        let's start with the straight forward and ignore the sortedness
        """
        for row in matrix:
            if target in row:
                return True

        return False