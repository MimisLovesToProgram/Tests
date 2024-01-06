minimum = None

def backtrack(nums):
    for i, num in enumerate(range(nums[0], 0, -1)):
        if len(nums) - 1 <= i + num:
            return minimum
        
    

class Solution:
    def jump(self, nums: list) -> int:
        minimum = len(nums)
        return backtrack(nums)