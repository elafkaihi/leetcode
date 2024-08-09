class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i,j = 0,len(height)-1
        while i < j :
            width = j - i
            h = min(height[i], height[j])
            area = width*h
            maxarea = max(maxarea, area)
            if height[i] < height[j]:
                i = i+1
            else:
                j = j-1
        return maxarea