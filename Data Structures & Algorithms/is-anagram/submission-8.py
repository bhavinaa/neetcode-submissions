class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    # letter : freq
        letters = {}
        def get_freq(word):
            letters = {}
            for i in range(0,len(word)):
                letter = word[i]
                letters[letter] = 1 + letters.get(letter,0)
                
            return letters
       
        return get_freq(s) == get_freq(t)
            
        