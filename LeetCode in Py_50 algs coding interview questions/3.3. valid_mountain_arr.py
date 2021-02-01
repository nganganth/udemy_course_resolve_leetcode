# 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/

from typing import List

# Time complexity: O(N) - 2 loops
# Space complexity: O(1) - constant - does not create any conditional memory
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        n = len(arr)
        if n <= 2:
            return False

        while i < n and arr[i] > arr[i - 1]:
            i += 1
        if i == 1 or i == n:
            return False
        while i < n and arr[i] < arr[i - 1]:
            i += 1
        return i == n

s = Solution()
print(s.validMountainArray([0,1,2,3,4,5,6,7,8,9]))

