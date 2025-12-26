class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hash1={}
        answer=[]
        for ch in nums:
            if ch in hash1:
                hash1[ch]=hash1[ch]+1
            else:
                hash1[ch]=1


        for c in hash1:
            if c==0:
                for i in range(hash1[c]):
                    answer.append(c)

        for c in hash1:
            if c==1:
                for i in range(hash1[c]):
                    answer.append(c)
                    
        for c in hash1:
            if c==2:
                for i in range(hash1[c]):
                    answer.append(c)

        nums[:]=answer


        
