#Problem
"""
There are several cards arranged in a row, and each card has an associated 
number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the 
row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""

#Solution
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        # if sum(cardPoints[:k]) > sum(cardPoints[-k:]):
        #     return sum(cardPoints[:k])
        # else:
        #     return sum(cardPoints[-k:])

        n = len(cardPoints)
        total_points = sum(cardPoints)
        window = n - k
        current_window_sum = sum(cardPoints[:window])
        min_window_sum = current_window_sum

        for i in range(window, n):
            current_window_sum += cardPoints[i] - cardPoints[i - window]
            min_window_sum = min(min_window_sum, current_window_sum)

        return total_points - min_window_sum
