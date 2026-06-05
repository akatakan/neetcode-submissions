class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq={}
        sub_freq={}
        for i in s1:
            freq[i]=freq.get(i,0) + 1
        L=0
        R=L+len(s1)-1
        while R < len(s2):
            sub = s2[L:R+1]
            print(sub)
            for i in sub:
                sub_freq[i]=sub_freq.get(i,0) + 1
            if freq == sub_freq:
                return True
            else:
                sub_freq={}
            L+=1
            R+=1
            
        return False