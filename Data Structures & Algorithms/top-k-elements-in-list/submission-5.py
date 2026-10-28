class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nf = {}
        for n in nums:
            nf[n] = nf.get(n, 0) + 1

        fn = {}
        for n in nf:
            freq = nf[n]
            if freq in fn:
                fn[freq].append(n)
            else:
                fn[freq] = [n]

        freqs = list(fn.keys())
        heapq.heapify_max(freqs)

        answer = []
        while len(answer) < k:
            max_freq = heapq.heappop_max(freqs)
            ns = fn[max_freq]
            answer += ns

        return answer[:k]