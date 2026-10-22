class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given numbers is non-decreasing (aka sorted), maybe we could use binary search. 

        For `n`, does `target-n` exist? If yes, then reutrn [indexN + 1, indexT +1 ]
        """

        def binary_search(nums: list[int], t: int) -> int:
            low = 0
            high = len(nums)-1
            mid = (low + high) // 2

            while low <= high:
                guess = nums[mid]
                #print(f"{low=} {mid=} {high=} {guess=} {t=}")
                if guess == t:
                    return mid
                elif guess > t:
                    high = mid - 1
                else:
                    low = mid + 1
                mid = (low + high) // 2

            return -1

        i = 0
        while i < len(numbers):
            n = numbers[i]
            b = target - n
            res = binary_search(numbers, b)
            if res == i:
                res += 1
            if res != -1:
                return [i+1, res+1]
            i += 1




