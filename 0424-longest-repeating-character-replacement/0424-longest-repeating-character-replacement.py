class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        hash={}
        repmax=0
        size=0
        for r in range (len(s)):
            
            if s[r] in hash:
                hash[s[r]]=hash[s[r]]+1
            else:
                hash[s[r]]=1

            repmax=max(repmax,hash[s[r]])
            
            while r-l+1-repmax>k:
                hash[s[l]]=hash[s[l]]-1
                if hash[s[l]]==0:
                    del hash[s[l]]
                l=l+1
            if r-l+1-repmax<=k:
                size=max(size,r-l+1)
                
        return size

            

                
                
                        