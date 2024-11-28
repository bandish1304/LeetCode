class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest = 0
        n = len(nums)
        end = 0
        far = 0
        
        for i in range(n-1):
            far = max(far, i + nums[i])
        
            if i == end:
                smallest += 1
                end = far
            
        return smallest
    
    #Time complexity:O(n)
    # Space complexity: O(1)