# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Array is sorted -> think binary search
# Time complexity: O(Log(N))
# Space complexity: O(1)
class Solution:
    # [Pseudocode]
    # left = 0
    # right = len(nums) - 1
    # while (left <= right):
    #     mid = (left + right)//2
    #     if (nums[mid] == target):
    #         if (mid == 0 || nums[mid - 1] != target):
    #             return mid
    #         right = mid - 1
    #     elif (nums[mid] > target):
    #         right = mid - 1
    #     else:
    #         left = mid + 1

    def getLeftPosition(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right)//2
            if (nums[mid] == target):
                if (mid - 1 >= 0 and nums[mid-1] != target or mid == 0):
                    return mid
                right = mid - 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def getRightPosition(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right)//2
            if (nums[mid] == target):
                if (mid + 1 < len(nums) and nums[mid + 1] != target or mid==len(nums) - 1):
                    return mid
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)

        return [left, right]
