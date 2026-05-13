# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        

        n= len(pairs)
        m=n//2
        L=pairs[:m]
        R=pairs[m:]
        k=i=j=0
        L=self.mergeSort(L)
        R=self.mergeSort(R)
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i+=1
            else:
                pairs[k]=R[j]
                j+=1
            k+=1

        while i < len(L):
            pairs[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            pairs[k] = R[j]
            j+=1
            k+=1
        return pairs
        
