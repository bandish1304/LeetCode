class Solution:
    def trailingZeroes(self, n: int) -> int:
        quotient = n
        numOfZeros = 0
        
        while True:
            quotient = quotient // 5
            numOfZeros += quotient
            if (quotient < 5):
                break
        return numOfZeros