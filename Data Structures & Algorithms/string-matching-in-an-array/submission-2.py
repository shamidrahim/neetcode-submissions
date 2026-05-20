class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def kmp(word1: str, word2: str) -> int:
            lps = [0] * len(word2)
            prevLPS, i = 0, 1
            while i < len(word2):
                if word2[i] == word2[prevLPS]:
                    lps[i] = prevLPS + 1
                    prevLPS += 1
                    i += 1
                elif prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]
            i = j = 0
            while i < len(word1):
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = lps[j - 1]

                if j == len(word2):
                    return i - len(word2)
            return -1

        res = []
        words.sort(key = len)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if kmp(words[j], words[i]) != -1:
                    res.append(words[i])
                    break
        return res

        