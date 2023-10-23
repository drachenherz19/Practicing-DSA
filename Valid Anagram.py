class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_cnt, t_cnt = {}, {}
        for i in range(len(s)):
            s_cnt[s[i]] = 1 + s_cnt.get(s[i],0)
            t_cnt[t[i]] = 1 + t_cnt.get(t[i],0)
        
        for x in s_cnt:
            if s_cnt[x] != t_cnt.get(x,0):
                return False
        
        return True
            