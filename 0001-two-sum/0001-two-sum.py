class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash1={}
        for i in range(len(nums)):
            if nums[i] in hash1:
                return [hash1[nums[i]],i]

            else:
                hash1[target-nums[i]]=i







            




                

            
