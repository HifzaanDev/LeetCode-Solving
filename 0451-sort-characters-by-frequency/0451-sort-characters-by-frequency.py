class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

   
        res=""
        hash={}
        for i in range(len(s)):
            if s[i] in  hash:
                hash[s[i]]=hash[s[i]]+1
            else:
                hash[s[i]]=1
        while hash:
            max_char=""
            max_count=0
            for ch in s:
                if ch in hash:
                    if hash[ch]>max_count:
                        max_count=hash[ch]
                        max_char=ch
            res=res+max_char*max_count
            del hash[max_char]
        return res
            
                        

