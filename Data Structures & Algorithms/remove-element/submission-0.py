class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        n = len(nums)
        for R in range(n):
            if nums[R] == val:
                continue
            nums[L] = nums[R]
            L += 1
        return L
                
            
                


                

                
            



                

        