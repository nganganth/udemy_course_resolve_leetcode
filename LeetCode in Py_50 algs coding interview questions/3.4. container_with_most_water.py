# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    # Time Limit Exceeded with big data 
    # Time complexity: O(N*N)
    # Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0

        for i in range(n):
            for j in range(i+1, n):
                max_area = max(max_area, min(height[i], height[j])*(j-i))
        return max_area
    
    # another approach 
    # Time complexity: O(N)
    # Space complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
            

            