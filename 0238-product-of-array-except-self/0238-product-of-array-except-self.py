class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        
        prod=1
        ans=[]
        
        for i in range(n):
            ans.append(prod)
            prod=prod*nums[i]
            
        m=len(ans)
        newprod=1
        for i in range(m-1,-1,-1):
            ans[i]=ans[i]*newprod
            newprod=newprod*nums[i]

            

        return ans



