class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        valuePair = [timestamp, value]
        if key in self.timeMap:
            self.timeMap[key].append(valuePair)
        else:
            self.timeMap[key] = [valuePair]
        print("Appending the value below to")
        print(self.timeMap[key])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            valuePairs = self.timeMap[key]
            if valuePairs[0][0] > timestamp:
                return ""

            l = 0
            r = len(valuePairs) - 1
            output = valuePairs[0]
            while l <= r:
                mid = (l + r) // 2
                if valuePairs[mid][0] <= timestamp:
                    output = valuePairs[mid]
                    l = mid + 1
                else:
                    r = mid - 1
            return output[1]
        else:
            return ""
