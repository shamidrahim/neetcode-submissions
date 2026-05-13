class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp.get(tmp, 0):
                return [mp.get(tmp, 0), i + 1]
            mp[numbers[i]] = i + 1
        return []
