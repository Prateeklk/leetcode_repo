class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        set_1 = {x for x in nums1}
        set_2 = {x for x in nums2}
        print(set_1)
        print(set_2)
        for i in set_2:
            if i in set_1:
                res.append(i)
        return res