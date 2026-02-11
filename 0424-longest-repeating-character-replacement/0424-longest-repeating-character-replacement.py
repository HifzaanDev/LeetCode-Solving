class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hash_count = {}
        max_freq=0
        max_len=0
        l=0

        #find max char count
        for i in range(len(s)):
            if s[i] in hash_count:
                hash_count[s[i]] = hash_count[s[i]]+1
            else:
                hash_count[s[i]]=1
        #updating max frequency accordingly
            if hash_count[s[i]]>max_freq:
                max_freq=hash_count[s[i]]
        #if condition fails move l forward 
            while i-l+1-max_freq>k:
                hash_count[s[l]]=hash_count[s[l]]-1
                l=l+1
            curr_len=i-l+1
        #update max_len 
            if curr_len>max_len:
                max_len=curr_len
        return max_len
