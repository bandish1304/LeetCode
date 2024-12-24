class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        
        if s == "": 
            return True
        if S > T:
            return False
        
        i = 0
        for j in range(T):
            if t[j] == s[i]:
                if i == S-1:
                    return True
                i += 1
                
        return False
                
        