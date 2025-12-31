class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen=[]
        n=len(nums)
        set_ans=set()
        nums.sort()
        for i in range(n-2):
            if nums[i] in seen:
                continue
            seen.append(nums[i])
            l=i+1
            r=n-1
            while l<r:
                if nums[l]+nums[r]+nums[i]>0:
                    r=r-1
                elif nums[l]+nums[r]+nums[i]<0:
                    l=l+1
                elif nums[l]+nums[r]+nums[i]==0:
                    set_ans.add((nums[l],nums[r],nums[i]))
                    l=l+1
                    r=r-1
        arr=list(set_ans)
        return arr