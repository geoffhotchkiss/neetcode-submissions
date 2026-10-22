class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        area = min(heights[i], heights[j]) * (j-i)
         0 1 2 3 4 5 6 7
        [1,7,2,5,4,7,3,6]
         ^             ^  --> min(1,6) * (7-0) = 7
           ^           ^  --> min(7,6) * (7-1) = 36 | move 
        """
        a = 0
        b = len(heights) - 1

        biggest = min(heights[a], heights[b]) * (b-a)

        while a < b:
            tmp = min(heights[a], heights[b]) * (b-a)
            if tmp > biggest:
                biggest = tmp

            if heights[a] <= heights[b]:
                a += 1
            else:
                b -= 1

        return biggest
        


