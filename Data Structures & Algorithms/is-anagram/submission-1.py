class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letter1 = {}
        letter2 = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in letter1:
                letter1[s[i]] +=1
            else:
                letter1[s[i]] = 1
            
            if t[i] in letter2:
                letter2[t[i]] +=1
            else:
                letter2[t[i]] = 1
        if letter1==letter2:
            print(letter1)
            print(letter2)
            return True
        return False