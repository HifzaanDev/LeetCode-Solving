class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        if target not in nums:
            return -1
        while l<=r:
            mid=(l+r)/2
            if target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
            elif target==nums[mid]:
                return mid