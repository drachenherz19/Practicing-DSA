class Solution:
    def search_insert(nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                low = mid + 1  # Adjust low pointer
            else:
                high = mid - 1  # Adjust high pointer

        return low  # Return the index for insertion position