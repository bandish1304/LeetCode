class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        
        while n != 0:
            output = output + 1
            n = n & (n-1)
        return output
    
    # time complexity: worst case-O(Bits)
    # space complexity: O(1)
        