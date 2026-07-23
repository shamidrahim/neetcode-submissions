class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        res = []
        slots1.sort()
        slots2.sort()
        s1 = s2 = 0
        while s1 < len(slots1) and s2 < len(slots2):
            start1, end1 = slots1[s1]
            start2, end2 = slots2[s2]
            minEnd = min(end1, end2)
            maxStart = max(start1, start2)
            if minEnd - maxStart >= duration:
                return [maxStart, maxStart + duration]
            
            if end1 < end2:
                s1 += 1
            else:
                s2 += 1
        return res


        