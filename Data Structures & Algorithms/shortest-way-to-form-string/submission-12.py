class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_length = len(source)
        next_occurence = [defaultdict(int) for idx in range(source_length)]
        next_occurence[source_length - 1][source[source_length - 1]] = source_length - 1
        for idx in range(source_length - 2, - 1, -1):
            next_occurence[idx] = next_occurence[idx + 1].copy()
            next_occurence[idx][source[idx]] = idx
        source_iterator = 0
        count = 1
        for char in target:
            if char not in next_occurence[0]:
                return -1
            if (source_iterator == source_length or char not in next_occurence[source_iterator]):
                count += 1
                source_iterator = 0
            source_iterator = next_occurence[source_iterator][char] + 1
        return count




        
        