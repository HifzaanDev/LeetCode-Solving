class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)

        hash={}
        answer=0
        for r in range(n):
            if nums[r] in hash:
                answer=r-hash[nums[r]]
                if answer<=k:
                    return True
               
            hash[nums[r]]=r
        return False
