class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def rabinKarp(word1:str, word2:str) -> int:
            base1, mod1 = 31, 10**9 + 7
            base2, mod2 = 37, 10**9 + 9
            n, m = len(word1), len(word2)
            power1 = pow(base1, m, mod1)
            power2 = pow(base2, m, mod2)

            word1_hash1 = word1_hash2 = 0
            word2_hash1 = word2_hash2 = 0
            for i in range(m):
                word1_hash1 = (word1_hash1 * base1 + ord(word1[i])) % mod1
                word1_hash2 = (word1_hash2 * base2 + ord(word1[i])) % mod2
                word2_hash1 = (word2_hash1 * base1 + ord(word2[i])) % mod1
                word2_hash2 = (word2_hash2 * base2 + ord(word2[i])) % mod2
            
            for j in range(n - m + 1):
                if word1_hash1 == word2_hash1 and word1_hash2 == word2_hash2:
                    return j
                
                if j + m < n:
                    word1_hash1 = (word1_hash1 * base1 - ord(word1[j]) * power1 
                    + ord(word1[j + m])) % mod1
                    word1_hash2 = (word1_hash2 * base2 - ord(word1[j]) * power2 
                    + ord(word1[j + m])) % mod2
                    word1_hash1 = (word1_hash1 + mod1) % mod1
                    word1_hash2 = (word1_hash2 + mod2) % mod2
            return -1
        res = []
        words.sort(key = len)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if rabinKarp(words[j], words[i]) != -1:
                    res.append(words[i])
                    break
        return res
            

        