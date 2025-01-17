#Problem
"""
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order. 
"""

#Solution
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-3):
            if i >0 and nums[i]== nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                l,r = j+1,len(nums)-1
                while l<r:
                    a = nums[i]+nums[j]+nums[l]+nums[r]
                    if a < target:
                        l+=1
                    elif a>target:
                        r-=1
                    else:
                        result.append((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        while nums[l] == nums[l-1] and l<r :
                            l+=1
        k = []
        for b in list(set(result)):
            k.append(list(b))
        return k        