class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-1):
            m=nums[i]
            for j in range(i+1,n):
                if nums[j]<m:
                    m=nums[j]
                    nums[i],nums[j]=nums[j],nums[i]