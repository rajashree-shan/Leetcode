class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1

        ans = ""

        while left <= right:

            mid = (left + right) // 2

            time = values[mid][0]
            value = values[mid][1]

            if time <= timestamp:
                ans = value
                left = mid + 1

            else:
                right = mid - 1

        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)