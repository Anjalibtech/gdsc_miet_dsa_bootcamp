class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p=set(nums)
        if len(p)==len(nums)-1:
            s1=sum(p)
            s2=sum(nums)
            return s2-s1
        else:
            for i in nums:
                if nums.count(i)>1:
                    return i