class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        words.sort(key=len)
        for i in range(0, len(words)):
            temp = words[i]
            for j in range(i + 1, len(words)):
                curr = words[j]
                if temp in curr:
                    result.add(temp)
        return list(result)

        