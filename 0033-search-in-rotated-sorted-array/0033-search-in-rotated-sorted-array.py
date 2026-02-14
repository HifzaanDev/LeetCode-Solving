class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        if target not in nums:
            return -1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]==nums[r]==nums[mid]:
                r=r-1
                l=l+1
                continue
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[l]>nums[mid]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
    

                    
