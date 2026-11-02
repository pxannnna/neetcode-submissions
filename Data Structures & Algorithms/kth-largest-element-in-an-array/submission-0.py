class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k

        def partition(low: int, high: int) -> int:
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]  #swap
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i #returns correct sorted position

        def quick_select(low: int, high: int) -> int:
            if low == high:
                return nums[low]

            pi = partition(low, high)

            if pi == target_idx:
                return nums[pi]
            elif pi > target_idx:
                return quick_select(low, pi - 1)
            else:
                return quick_select(pi + 1, high)

        return quick_select(0, len(nums) - 1)