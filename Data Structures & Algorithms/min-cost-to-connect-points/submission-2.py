class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                manDist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((manDist, j))
                adj[j].append((manDist, i))
        
        visit = set()
        res = 0
        minHeap = [[0, 0]]

        while minHeap:
            dist, point = heapq.heappop(minHeap)

            if point in visit:
                continue
            res += dist
            visit.add(point)

            for dist2, point2 in adj[point]:
                if point2 not in visit:
                    heapq.heappush(minHeap, [dist2, point2])
        return res

       