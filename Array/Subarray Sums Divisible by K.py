#Problem Statement
"""
Given an integer array nums and an integer k, return the number of non-empty 
subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
"""

#Solution
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1} 
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder < 0:
                remainder += k

            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count
