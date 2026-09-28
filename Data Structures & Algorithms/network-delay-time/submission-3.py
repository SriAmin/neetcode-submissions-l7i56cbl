class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        time = 0
        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        return time if len(visited) == n else -1