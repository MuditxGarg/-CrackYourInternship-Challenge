#Problem Description
"""
Given an array of integers nums containing n + 1 integers where each integer 
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and 
uses only constant extra space.
"""

#solution
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1 = sorted(nums)
        for i in range(len(l1)):
            if l1[i] == l1[i+1]:
                return l1[i]
                break        