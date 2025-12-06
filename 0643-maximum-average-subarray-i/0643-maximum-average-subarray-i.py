class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        local_sum=sum(nums[:k])
        max_sum=sum(nums[:k])
        for r in range(k,n):
            local_sum=local_sum+nums[r]-nums[r-k]
            max_sum=max(local_sum,max_sum)
        max_avg=max_sum/float(k)
        return max_avg