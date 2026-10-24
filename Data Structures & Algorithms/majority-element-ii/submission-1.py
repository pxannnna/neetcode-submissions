class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        minimum = len(nums) // 3
        added = set()
        res = []
        for num in nums:
            count[num] += 1
            if count[num] > minimum and num not in added:
                res.append(num)
                added.add(num)
        return res