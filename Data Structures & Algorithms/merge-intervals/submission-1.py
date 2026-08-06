class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        tmpInt = intervals[0]
        output = []
        for i in range(1, len(intervals)):
            if tmpInt[0] <= intervals[i][1] and intervals[i][0] <= tmpInt[1]:
                tmpInt = [min(tmpInt[0], intervals[i][0]), max(tmpInt[1], intervals[i][1])]
            else:
                output.append(tmpInt)
                tmpInt = intervals[i]
        output.append(tmpInt)
        print(output)
        return output