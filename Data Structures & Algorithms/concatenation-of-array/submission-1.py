class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = [0]*2*len(nums)
        for i,n in enumerate(nums):
            answer[i], answer[i+len(nums)] = n, n

        return answer