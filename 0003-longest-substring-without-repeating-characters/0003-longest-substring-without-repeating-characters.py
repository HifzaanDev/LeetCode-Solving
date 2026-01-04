class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        elif len(s)==1:
            return 1
        seen=[]
        l=0
        answer=0
        for i in range(0,len(s)):
            if s[i] in seen:
                answer=max(answer,i-l)
                l=i
                seen.remove(s[i])
                seen.append(s[i])
            elif s[i] not in seen:
                seen.append(s[i])
        if len(s) == len(set(seen)):
            return len(s)
        
        return answer

