class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        nums.sort()
        best=float("inf")
        final=0
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1

            while l<r:
                curr=nums[i]+nums[l]+nums[r]
                if best>abs(target-curr):
                    final=curr
                    best=abs(target-curr)
                if curr<target:
                    l=l+1
                if curr>target:
                    r=r-1
                if curr==target:
                    return curr
        return final



            
