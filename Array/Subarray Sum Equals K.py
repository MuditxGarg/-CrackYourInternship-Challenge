#Problem
"""
Given an array of integers nums and an integer k, return the total number 
of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

#Solution
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        current_sum = 0
        sum_dict = {0: 1} 
    
        for num in nums:
            current_sum += num
            if current_sum - k in sum_dict:
                count += sum_dict[current_sum - k]
            if current_sum in sum_dict:
                sum_dict[current_sum] += 1
            else:
                sum_dict[current_sum] = 1
        
        return count