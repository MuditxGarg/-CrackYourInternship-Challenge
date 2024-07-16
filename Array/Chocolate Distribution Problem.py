#Problem Statement

'''
Given an array A[ ] of positive integers of size N, where each value represents 
the number of chocolates in a packet. Each packet can have a variable number of chocolates. 
There are M students, the task is to distribute chocolate packets among M students such that :

1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum 
number of chocolates given to a student is minimum.

Your Task:
You don't need to take any input or print anything. Your task is to complete the function 
findMinDiff() which takes array A[ ], N and M as input parameters and returns the minimum 
possible difference between maximum number of chocolates given to a student and minimum 
number of chocolates given to a student.
'''

#Solution
#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        if (M == 0 or N == 0):
            return 0
            
        A.sort()
        min_diff = A[N-1] - A[0]
        
        if (N < M):
            return -1
            
        for i in range(N - M + 1):
            current_diff = A[i + M - 1] - A[i]
            if current_diff < min_diff:
                min_diff = current_diff

        return min_diff
        


#{ 
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends