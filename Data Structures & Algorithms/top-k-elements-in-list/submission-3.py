class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for n in nums:
            num_counts[n] = num_counts.get(n, 0) + 1
        
        max_counts = []
        # max counts is a list of (n,nfreq) where n 

        for n in num_counts:
            freq = num_counts[n]
            if len(max_counts) < k:
                max_counts.append((n, freq))
            else:
                # our max_counts list is seeded
                # now for each remaining (n, freq), if (n, freq) is larger than all of them, we replace the smallest with it
                smallest_index = 0
                smallest_freq = max_counts[smallest_index][1]
                #print(f"{max_counts=} {n=} {freq=}")

                for index,(m,mfreq) in enumerate(max_counts):
                    if mfreq < smallest_freq:
                        smallest_index = index
                        smallest_freq = mfreq

                if freq > smallest_freq:
                    max_counts[smallest_index] = (n, freq)


        return [n for (n,c) in max_counts]