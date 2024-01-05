from typing import List # Only necessary for VS code, remove this line in LeetCode.

def recursive_solution(nums, index, memo):
    if index >= len(nums) - 1:
        return True

    if memo[index] is not None:
        return memo[index]

    for jump_space in range(nums[index], 0, -1):
        if recursive_solution(nums, index + jump_space, memo):
            memo[index] = True
            return True

    memo[index] = False
    return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)
        return recursive_solution(nums, 0, memo)
