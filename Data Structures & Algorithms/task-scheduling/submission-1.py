class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = Counter(tasks)
        maxHeap = [-cnt for cnt in taskFreq.values()]
        heapq.heapify(maxHeap)

        cycle = 0
        q = deque()

        while maxHeap or q:
            cycle += 1

            if not maxHeap:
                cycle = q[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count != 0:
                    q.append([count, cycle + n])
            if q and q[0][1] == cycle:
                heapq.heappush(maxHeap, q.popleft()[0])

        return cycle
