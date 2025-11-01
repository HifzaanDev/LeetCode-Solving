class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        depth=0
        res=""
        for ch in s:
            if ch=="(":
                if depth>0:
                    res=res+"("
                    depth=depth+1
            else:
                
                depth=depth-1
                if depth>0:
                    res=res+")"

