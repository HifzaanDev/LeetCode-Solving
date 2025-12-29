class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set(nums)
        max_len=0
        
        for n in seen:
            
            if n-1 not in seen:
                length=1
                while n+length in seen:
                    length=length+1

                max_len=max(max_len,length)
        return max_len
