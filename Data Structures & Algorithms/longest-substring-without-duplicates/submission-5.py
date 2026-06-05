class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        R=0
        longS=set()
        lenS=0
        while R < len(s):
            if s[R] in longS:
                longS.discard(s[L])
                L+=1
            else:
                longS.add(s[R])
                lenS=max(lenS,len(longS))
                R+=1
        return lenS