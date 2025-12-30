class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set(nums)
        max_len=0
        for ch in seen:
            if ch-1 not in seen:
                length=1
                while ch+length in seen:
                    length=length+1
                max_len=max(length,max_len)

        return max_len
