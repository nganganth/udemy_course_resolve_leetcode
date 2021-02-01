# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

# Count the number of non-zero elements and move them to the beginning of the array in order
# That means that, starting from counted value till end of the array, rest of values are zero.

from typing import List
# Time Complexity: O(2*N) = O(N)
# Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
        print(nums)
    
s = Solution()
s.moveZeroes([0, 2, 0, 5, 6, 7])
