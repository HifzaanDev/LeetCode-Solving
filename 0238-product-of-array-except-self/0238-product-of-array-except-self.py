class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_count=0
        non_zero_prod=1
        prod=1
        final_ans=[]
        for ch in nums:
            if ch==0:
                zero_count=zero_count+1
                if zero_count>1:
                    non_zero_prod=0
                    break
            elif ch !=0:
                non_zero_prod=non_zero_prod*ch
        for char in nums:
            prod=prod*char
        for c in nums:
            if c !=0:
                ans=prod/c
                final_ans.append(ans)
            else:
                ans=non_zero_prod
                final_ans.append(ans)

        return final_ans

