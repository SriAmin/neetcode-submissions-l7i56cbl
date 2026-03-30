class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq[i] + 1 if i in freq else 1
        mini_heap = []

        for num in freq.keys():
            heapq.heappush(mini_heap, (freq[num], num))
            if len(mini_heap) > k:
                heapq.heappop(mini_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(mini_heap)[1])
        return res
        
        freqList = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        output = []
        for i in range(k):
            output.append(freqList[i][0])
        
        return output