#User function Template for python3


class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        i=bin(N)
        s=[0]
        j=0
        for k in range(2,len(i)):
            if i[k]=='0':
                s.append(0)
                j+=1
            if i[k]=='1':
                s[j]+=1
        return max(s)

#{
#Driver Code Starts
#Initial Template for Python 3

import math

def main():
    T=int(input())
    
    while(T>0):
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T=-1


if __name__ == "__main__":
    main()
#} Driver Code Ends
