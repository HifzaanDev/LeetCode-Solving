class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash1={}
        for i in range  (len(nums)):
            if nums[i] in hash1:
                hash1[nums[i]]=hash1[nums[i]]+1
            else:
                hash1[nums[i]]=1
        for ch in hash1:
            if hash1[ch]>=2:
                return True

        return False