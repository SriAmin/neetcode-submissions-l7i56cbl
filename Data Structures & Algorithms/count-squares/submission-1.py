class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.points:
            if (abs(qx - x) != abs(qy - y)) or x == qx or y == qy:
                continue
            res += self.pointsCount.get((x, qy), 0) * self.pointsCount.get((qx, y), 0)
        return res

    