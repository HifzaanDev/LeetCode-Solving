class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash1={}
        max=0
        curr_big=0

        arr=[]
        for num in nums:
            if num in hash1:
                hash1[num]=hash1[num]+1
            else:
                hash1[num]=1
        for i in range(k):
            
            for ch in hash1:
                if hash1[ch]>max:
                    max=hash1[ch]
                    curr_big=ch
            del hash1[curr_big]
            arr.append(curr_big)
            max=0

        return arr
