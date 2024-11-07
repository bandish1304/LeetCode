class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carryOn = 0
        result = ""
        
        a, b = list(a), list(b)
        
        while a or b or carryOn == 1:
            if a:
                carryOn += int(a.pop())
            if b:
                carryOn += int(b.pop())
                
            result += str(carryOn % 2)
            carryOn = carryOn // 2
            
        return result[::-1]
        