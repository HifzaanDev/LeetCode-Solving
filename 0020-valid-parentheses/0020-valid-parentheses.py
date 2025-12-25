class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack=[]
        hash1={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in hash1:
                if stack and hash1[ch]==stack[-1]:
                    stack.pop(-1)
                elif stack and hash1[ch] != stack[-1]:
                    return False
                elif stack==[]:
                    return False

            else:
                stack.append(ch)
        if stack==[]:
            return True
        return False
                

