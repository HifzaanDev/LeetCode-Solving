class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash1={}
        top_k=[]
        for ch in nums:
            if ch in hash1:
                hash1[ch]=hash1[ch]+1
            else:
                hash1[ch]=1
        for i in range(k):
            max_rep=0
            max_ele=0
            for c in hash1:
                if hash1[c]>max_rep:
                    max_rep=hash1[c]
                    max_ele=c

            top_k.append(max_ele)
            del hash1[max_ele]
        return top_k
        

