class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        top_sort = []
        visit = set()
        path = set()
        def dfs(src, visit, path, adj):
            if src in visit:
                return True
            if src in path:
                return False
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei, visit, path, adj):
                    return False
            visit.add(src)
            top_sort.append(src)
            path.remove(src)
            return True
        for i in range(n):
            if not dfs(i, visit, path, adj):
                return []
        top_sort.reverse()

        return top_sort
    
        