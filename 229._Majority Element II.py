class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = defaultdict(int)
        n = len(nums)
        res = []
        for num in nums:
            m[num]+=1

        for key,val in m.items():
            if val > n//3:
                res.append(key)
        return res