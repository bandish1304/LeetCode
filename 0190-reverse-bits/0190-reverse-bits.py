class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for _ in range(0,32):
            output <<= 1
            if n & 1:
                output += 1
            n >>= 1
        return output
            
        