class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        hash = [0] * (n + 1)
        
        for i in range(n):
            hash[A[i]]+=1
            
        repeat,missing = -1,-1
        for i in range(1,n+1):
            if hash[i] == 2:
                repeat = i
            elif hash[i] == 0:
                missing = i
            if missing!=-1 and repeat !=-1:
                break
        return [repeat,missing]

