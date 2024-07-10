class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count+=1
            else:
                product*=nums[i]

        if zero_count > 1:
            for i in range(len(nums)):
                res.append(0)
        if zero_count == 0:
            for j in range(len(nums)):
                res.append(product//nums[j])
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(product)
                else:
                    res.append(0)
        return res

            