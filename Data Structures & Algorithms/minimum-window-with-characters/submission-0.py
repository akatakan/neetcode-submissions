class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        L=0
        R=0
        t_freq = {}
        for i in t:
            t_freq[i] = t_freq.get(i,0) + 1
        s_freq = {}
        have=0
        need=len(t_freq)
        min_sub_len=float("inf")
        start,end=-1,-1
        while R < len(s):
            char = s[R]
            s_freq[char] = s_freq.get(char,0) + 1
            if char in t_freq and s_freq[char] == t_freq[char]:
                have+=1
            while have == need:
                if (R - L + 1) < min_sub_len:
                    min_sub_len = R - L + 1
                    start=L
                    end=R
                if s[L] in t_freq and s_freq[s[L]] == t_freq[s[L]]:
                    have-=1
                s_freq[s[L]]-=1
                L+=1
            R+=1
        return s[start:end+1]
