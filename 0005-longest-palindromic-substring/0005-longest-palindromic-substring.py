class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        max_len=1
        start=0
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if max_len<r-l+1:
                    max_len=r-l+1
                    start=l
                l=l-1
                r=r+1
            l=i
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                if max_len<r-l+1:
                    max_len=r-l+1
                    start=l
                l=l-1
                r=r+1

        return s[start:start+max_len]
