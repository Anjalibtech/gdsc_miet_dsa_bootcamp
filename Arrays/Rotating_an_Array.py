class Solution:
    def leftRotate(self, arr, n, d):
        # code hereclass Solution:
        f=arr[:d]
        for i in range(d):
            arr.pop(0)
        arr.extend(f)
