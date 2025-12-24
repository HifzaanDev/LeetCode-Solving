class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash1={}
        answer=[]
        n=len(nums)
        k=0
        for i in range (n):
            if nums[i] in hash1:
                hash1[nums[i]]=hash1[nums[i]]+1
            else:
                hash1[nums[i]]=1

        for ch in hash1:
            if hash1[ch]==1:
                answer.append(ch)
                k=k+1
            if hash1[ch]>1:
                answer.append(ch)
                k=k+1
                hash1[ch]=0
        answer.sort()
        nums[:] = answer
        return k


