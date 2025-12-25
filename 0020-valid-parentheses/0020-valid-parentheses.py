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
                if stack==[]:
                    return False
                elif hash1[ch]==stack[-1]:
                    stack.pop(-1)
                elif hash1[ch] != stack[-1]:
                    return False


            else:
                stack.append(ch)
        if stack==[]:
            return True
        return False
                

