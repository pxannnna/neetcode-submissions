import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        max_value = 0
        
        res = []
        max_heap = [(-nums[i], i) for i in range(k)] #add first k elements 
        heapq.heapify(max_heap)
        res.append(-max_heap[0][0])
        

        for l in range(1, len(nums)-k+1):
            r = l + k - 1
            heapq.heappush(max_heap, (-nums[r], r))

            # Remove elements from top if their index is out of window (< l)
            while max_heap[0][1] < l:
                heapq.heappop(max_heap)

            # Read top of heap from index 0
            value = max_heap[0][0]
            res.append(-value)

        return res

