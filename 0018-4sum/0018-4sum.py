class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        answer=[]
        hash1={}
        final=[]
        n=len(nums)
        for i in range(len(nums)):
            for j in range(i+1,n,1):
                l=j+1
                r=len(nums)-1
                while l<r:
                    curr=nums[i]+nums[j]+nums[l]+nums[r]
                    if curr<target:
                        l=l+1
                    if curr>target:
                        r=r-1
                    if curr==target:
                        local=[]
                        answer.append([nums[i],nums[j],nums[r],nums[l]])
                        l=l+1
                        r=r-1
        for i in range(len(answer)):
            t=tuple(answer[i])
            if t in hash1:
                hash1[t]=hash1[t]+1
            else:
                hash1[t]=1
        for ch in hash1:
            if hash1[ch]==1:
                final.append(ch)
            if hash1[ch]>1:
                final.append(ch)
                hash1[ch]==0

        return final
        
