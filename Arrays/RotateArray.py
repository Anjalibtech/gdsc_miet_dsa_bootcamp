class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            p=nums[-1]
            nums.pop(-1)
            nums.insert(0,p)