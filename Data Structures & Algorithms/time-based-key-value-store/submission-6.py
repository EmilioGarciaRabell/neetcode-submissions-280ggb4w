from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value
            
            

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeMap:
            return ""
        
        if timestamp in self.timeMap[key]:
            return self.timeMap[key][timestamp]
            
        timeStampList = list(self.timeMap[key].keys())
        l = 0
        r = len(timeStampList) - 1
        res = ""
        
        while l <= r:
            m = (l + r)//2
            if timeStampList[m] <= timestamp:
                res = timeStampList[m]
                l = m + 1
            else:
                r = m - 1
        return self.timeMap[key][res] if res != "" else ""
