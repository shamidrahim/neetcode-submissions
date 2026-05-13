class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum, avg, res = 0, 0, 0
        L = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                sum -= arr[L]
                L += 1
            sum+=arr[R]
            avg = sum//k
            if avg >= threshold and R - L + 1 == k:
                res += 1
        return res
            
        
            

            
        