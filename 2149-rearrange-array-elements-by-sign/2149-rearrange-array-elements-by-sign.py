class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])


        res=[]
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res