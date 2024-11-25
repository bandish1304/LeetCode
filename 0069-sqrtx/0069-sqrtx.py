class Solution:
    def mySqrt(self, x: int) -> int:
        L = 1
        R = x
        
        while L <= R:
            m = (L + R) // 2
            squared = m * m
            
            if squared == x:
                return m
            elif squared < x:
                L =  m + 1
            else:
                R = m -1
        return R
            
        