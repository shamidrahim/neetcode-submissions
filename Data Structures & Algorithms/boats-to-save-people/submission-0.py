class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                r -= 1
                l += 1
            elif people[l] + people[r] > limit:
                if people[r] <= limit:
                    res += 1
                    r -= 1
        return res