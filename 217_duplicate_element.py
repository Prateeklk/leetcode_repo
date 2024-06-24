class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for i in range(len(nums)):
            res.add(nums[i])

        if len(res) < len(nums):
            return True
        return False
        