class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr=[]
        cleaned_str="".join(s.split())
        final_cleaned=cleaned_str.lower()
        for ch in final_cleaned:
            if ch.isalnum():
                newstr.append(ch)

        l=0
        r=len(newstr)-1

        while l<=r:
            if newstr[l]==newstr[r]:
                l=l+1
                r=r-1

            else:
                return False

        return True
