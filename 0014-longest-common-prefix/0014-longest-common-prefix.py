class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        
        for letters in strs:
            if len(letters) < min_length:
                min_length = len(letters)
                
        i = 0
        while i < min_length:
            for letters in strs:
                if letters[i] != strs[0][i]:
                    return letters[:i]
            i = i + 1
            
        return letters[:i]
                    
            