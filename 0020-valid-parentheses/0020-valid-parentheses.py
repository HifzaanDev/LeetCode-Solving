class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack=[]
        hash1={')':'(','}':'{',']':'['}
        for c in s:
            if c in hash1:
                if stack==[]:
                    return False
                elif stack[-1]==hash1[c]:
                    stack.pop(-1)
                elif stack[-1] != hash1[c]:
                    return False
            else:
                stack.append(c)
        if stack==[]:
            return True 

        return False

            

