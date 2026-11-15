class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        word = ""
        for i in range(0, len(s)):
            v = s[i].lower()
            if v.isalnum():
                word = word + v
        print(word)
        return word == word[::-1]

       
            