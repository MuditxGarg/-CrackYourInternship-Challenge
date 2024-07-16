#Problem Statement
"""
Given an integer array nums of length n where all the integers of nums are in the 
range [1, n] and each integer appears once or twice, return an array of all the 
integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space
"""

#Solution
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        return ans