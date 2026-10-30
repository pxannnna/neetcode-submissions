from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        timeMap = self.timeMap
        values = timeMap[key]
        res = ""
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            val, t = values[mid]

            if t <= timestamp:
                res = val
                left = mid + 1
            else:
                right = mid - 1
        return res


        
