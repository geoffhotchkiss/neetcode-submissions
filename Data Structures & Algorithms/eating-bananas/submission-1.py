class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_bananas = max(piles)

        if len(piles) == h:
            return min_bananas

        def simulate(piles, k) -> int:
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/k)
            
            return total_time


        low, high = 1, min_bananas

        while low <= high:
            guess = (low + high) // 2

            time = simulate(piles, guess)

            # if we finish before the time limit, we're eating too fast and should try a lower rate
            if time <= h:
                min_bananas = guess
                high = guess - 1
            else: 
                # we're not eating fast enough, so we need to try a higher rate
                low = guess + 1

        return min_bananas