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
        for i in s2[:len(s1)]:
            sub_freq[i]=sub_freq.get(i,0) + 1
        while R < len(s2):
            if freq == sub_freq:
                return True
            sub_freq[s2[L]] = sub_freq[s2[L]]-1
            if sub_freq[s2[L]] ==0:
                del sub_freq[s2[L]]
            L+=1
            R+=1
            if R < len(s2):
                sub_freq[s2[R]] = sub_freq.get(s2[R],0)+1
        return False