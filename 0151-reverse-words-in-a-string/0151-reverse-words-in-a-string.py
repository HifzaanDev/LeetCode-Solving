class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitArr=s.split()
        reversedArr=reversed(splitArr)
        res= " ".join(reversedArr)
        return res
