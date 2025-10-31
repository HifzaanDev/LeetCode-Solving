class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=-1

        for j in range (n-2,-1,-1):
            if nums[j]<nums[j+1]:
                i=j
                break
        if i==-1:    
            nums.reverse()
            return(nums)
        for j in range(n-1,-1,-1):
            if nums[i]<nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                nums[i+1:] = reversed(nums[i+1:])
                break;
        return (nums)
              

            