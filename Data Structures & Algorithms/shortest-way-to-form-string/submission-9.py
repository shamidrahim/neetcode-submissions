class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        char_to_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_to_indices[c].append(i)
        
        def binary_search(indices, source_iterator):
            left, right = 0, len(indices) - 1
            result = len(indices)
            while left <= right:
                mid = (left + right) // 2
                if indices[mid] == source_iterator:
                    return mid
                elif indices[mid] < source_iterator:
                    left = mid + 1
                else:
                    result = mid
                    right = mid - 1
            return result
        
        source_iterator = 0
        count = 1
        for c in target:
            if c not in char_to_indices:
                return -1
            indices = char_to_indices[c]
            index = binary_search(indices, source_iterator)
            if index == len(indices):
                count += 1
                source_iterator = indices[0] + 1
            else:
                source_iterator = indices[index] + 1
        return count




        
        