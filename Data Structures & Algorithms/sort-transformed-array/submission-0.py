class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(x):
            return (a * x * x) + (b * x) + c

        res = []
        l, r = 0, len(nums) - 1

        if a < 0:
            while l <= r:
                l_transformed = transform(nums[l])
                r_transformed = transform(nums[r])
                if l_transformed < r_transformed:
                    res.append(l_transformed)
                    l += 1
                else:
                    res.append(r_transformed)
                    r -= 1
        else:
            while l <= r:
                l_transformed = transform(nums[l])
                r_transformed = transform(nums[r])
                if l_transformed > r_transformed:
                    res.append(l_transformed)
                    l += 1
                else:
                    res.append(r_transformed)
                    r -= 1
            res.reverse()
        return res

        