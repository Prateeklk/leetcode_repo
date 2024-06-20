class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        right = len(height) - 1
        left = 0
        while(left < right):
            min_val = min(height[left], height[right])
            temp = 1git 
            temp = min_val * (right - left)
            result = max(temp,result)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
            
        return result
            

        