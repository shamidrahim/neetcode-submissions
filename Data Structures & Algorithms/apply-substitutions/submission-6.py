class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replace_map ={key: value for key, value in replacements}
        resolved = {}
        for key in replace_map:
            self.resolve(key, replace_map, resolved)
        parts = text.split('%')
        res = []
        for i in range(len(parts)):
            if i % 2 == 0:
                res.append(parts[i])
            else:
                res.append(resolved[parts[i]])
        return ''.join(res)

    def resolve(self, key, replace_map, resolved):
        if key in resolved:
            return resolved[key]
        val = replace_map[key]
        if '%' not in val:
            resolved[key] = val
        parts = val.split('%')
        res = []
        for i in range(len(parts)):
            if i % 2 == 0:
                res.append(parts[i])
            else:
                res.append(self.resolve(parts[i], replace_map, resolved))
        resolved[key] = ''.join(res)
        return resolved[key]
        
