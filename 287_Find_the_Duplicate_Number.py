class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = [0] * (len(nums) + 1)            
        for i in range(len(nums)):
            if ans[nums[i]] == 0:
                ans[nums[i]] += 1
            else:
                return nums[i]
                
        return 0