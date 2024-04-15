class Solution:
    def maxLen(self, n, arr):
        #Code here
        mapp= {}
        maxi = 0
        sum = 0
        
        for i in range(n):
            sum+=arr[i]
            if sum == 0:
                maxi = i + 1
            else:
                if sum in mapp:
                    maxi = max(maxi,i-mapp[sum])
                else:
                    mapp[sum] = i
        return maxi

                
                
            