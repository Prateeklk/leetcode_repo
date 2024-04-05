class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        arr = set(nums)

        for num in arr:
            if (num-1) not in arr:
                curr_len = 1
                next_num = num + 1
                while(next_num) in arr:
                    curr_len += 1
                    next_num +=1
                max_len = max(max_len,curr_len)
        return max_len



        

            