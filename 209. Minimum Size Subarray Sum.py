class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)
        summ = 0
        left = 0

        if sum(nums) < target:
            return 0

        for i in range(len(nums)):
            summ += nums[i]
            while(summ >= target):
                res = min(res,i - left + 1)
                summ -= nums[left]
                left = left + 1
                
        return res
                
        
