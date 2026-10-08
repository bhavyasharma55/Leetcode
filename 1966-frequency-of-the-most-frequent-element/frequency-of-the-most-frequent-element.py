class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(); l = s = 0
        for r, x in enumerate(nums):
            s += x
            if x * (r - l + 1) - s > k:
                s -= nums[l]; l += 1
        return len(nums) - l