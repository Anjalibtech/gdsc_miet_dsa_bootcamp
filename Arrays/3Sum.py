class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        p=[]
        l=[]
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        if(set([nums[i],nums[k],nums[j]])) not in p:
                            p.append(set([nums[i],nums[j],nums[k]]))
                            l.append([nums[i],nums[j],nums[k]])

        return l