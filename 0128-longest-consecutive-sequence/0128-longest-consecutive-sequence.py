class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest=0
        numsetter=set(nums)
        for n in numsetter:
            if n-1 not in numsetter:
                length=1
                while n+length in numsetter:
                    length=length+1
                longest=max(longest,length)
        return(longest)