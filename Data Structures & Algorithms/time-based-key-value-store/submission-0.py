class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        closest = ""
        pairs = self.map.get(key,[])
        l = 0
        r = len(pairs) - 1

        while r >= l:
            m = (r + l) // 2
            
            t = pairs[m][0]
            if t == timestamp:
                return pairs[m][1]
            elif t < timestamp:
                l = m + 1
                closest = pairs[m][1]
            else:
                r = m - 1
        return closest
        




        
