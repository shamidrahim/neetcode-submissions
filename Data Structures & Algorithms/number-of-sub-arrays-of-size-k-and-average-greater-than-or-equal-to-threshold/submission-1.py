class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cursum = sum(arr[:k - 1])
        for L in range(len(arr) - k + 1):
            cursum += arr[L + k - 1]
            if (cursum / k) >= threshold:
                res += 1
            cursum -= arr[L]
        return res
            
        
            

            
        