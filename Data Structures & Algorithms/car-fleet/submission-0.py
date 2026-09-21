class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        postospeed = {}

        for i in range(len(position)):
            postospeed[position[i]] = speed[i]

        fleet = 0
        current_time = 0
        
        for p in sorted(postospeed.keys(), reverse = True):
            s = postospeed[p]
            time = (target - p) / s 

            if time > current_time:
                fleet += 1
                current_time = time
        return fleet
