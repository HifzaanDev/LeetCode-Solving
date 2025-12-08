class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hash1={}
        hash2={}
        l=0
        for i in range(len(s1)):
            if s1[i] in hash1:
                hash1[s1[i]]=hash1[s1[i]]+1
            else:
                hash1[s1[i]]=1

        for r in range(len(s2)):
            if s2[r] in hash2:
                hash2[s2[r]]=hash2[s2[r]]+1
            else:
                hash2[s2[r]]=1     

            if r-l+1>len(s1):
                hash2[s2[l]]=hash2[s2[l]]-1
                if  hash2[s2[l]]==0:
                    del  hash2[s2[l]]
                l=l+1

            if r-l+1==len(s1):
                if hash1==hash2:
                    return True
        return False
