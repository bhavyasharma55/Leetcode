class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Compare mid with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # Descending slope: a peak must exist on the left side (including mid)
                right = mid
            else:
                # Ascending slope: a peak must exist on the right side
                left = mid + 1

        # left == right points to a peak element
        return left