class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        def resolve(s):
            start = s.find('%')
            if start == -1:
                return s
            end = s.find('%', start + 1)
            if end == -1:
                return s
            var = s[start + 1: end]
            replace_val = resolve(replace_dict[var])

            return s[:start] + replace_val + resolve(s[end + 1:])
        replace_dict = {key:val for key, val in replacements}
        return resolve(text)
        
