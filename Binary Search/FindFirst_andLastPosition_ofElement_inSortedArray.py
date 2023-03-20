class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f=l=-1
        for i in range(len(nums)):
            if nums[i]==target:
                f=i
                break
        p=len(nums)
        for i in range(len(nums)):
            if nums[p-i-1]==target:
                l=p-i-1
                break
        return [f,l]