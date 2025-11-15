class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        seen=set()
        maxl=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left=left+1
            seen.add(s[right])
            maxl=max(maxl,(right-left)+1)
        return maxl