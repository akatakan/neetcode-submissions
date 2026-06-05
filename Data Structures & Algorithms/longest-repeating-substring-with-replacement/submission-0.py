class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L=0
        R=0
        diff={}
        max_len=0
        max_freq=0
        while R < len(s):
            diff[s[R]] = diff.get(s[R],0) + 1
            if diff[s[R]] > max_freq:
                max_freq = diff[s[R]]
            if ((R-L+1) - max_freq) > k:
                diff[s[L]] -=1
                L+=1
            else:
                max_len = max(max_len,R-L+1)
            R+=1
        return max_len