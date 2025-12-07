class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length=float("inf")
        n=len(nums)
        l=0
        sum=0
        for r in range(n):
            sum=sum+nums[r]



            while sum>=target:
                length=min(length,r-l+1)
                sum=sum-nums[l]
                l=l+1



        if length==float("inf"):
            return 0
        else:
            return length