class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # sort
        # try middle number as a weight limit
        # not enough? increase

        l, r = max(weights), sum(weights)
        res = r
        def canShip(cap):
            d, currCap = 1, cap

            for w in weights:
                
                if currCap - w < 0: 
                    d += 1
                    currCap = cap # new day, fresh capacity
                currCap -= w
            return d <= days 

        while l <= r:
            cap = (l+r) // 2 #capapcity of the ship
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1 #try smaller capacity
            else:
                l = cap + 1 #try larger capacity
        return res


 


        