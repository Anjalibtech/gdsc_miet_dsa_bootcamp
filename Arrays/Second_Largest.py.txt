class Solution:

	def print2largest(self,arr, n):
	    arr=set(arr)
		p=sorted(arr)
		if len(p)==1:
		    return -1
		else:
		    return p[-2]
