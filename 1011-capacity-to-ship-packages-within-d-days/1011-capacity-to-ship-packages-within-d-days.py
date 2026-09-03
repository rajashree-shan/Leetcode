class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        def canShip(capacity):
            used_days=1
            current=0
            for w in weights:

                if current+w>capacity:
                    used_days+=1
                    current=0
                
                current+=w

            return used_days<=days
        while l<r:

            mid=(l+r)//2
            if canShip(mid):
                r=mid
            else:
                l=mid+1

        return l 