'''
i'd like to keep a running list in memos 

to start, will have a list of the first 3 unique numbers 

then as a i go along, i need to keep track of how many times those numbers appear and if any overtake, i replace 



'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        answer = []
        topK_counts = sorted(counts.values())[-k:]
        for n, count in counts.items():
            if count in topK_counts:
                answer.append(n)

        return answer

            


