class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        output=[]
        n=len(numbers)
        l=0
        r=n-1
        
        while l<r:
            if numbers[l]+numbers[r]==target:
                output.append(l+1)
                output.append(r+1)
                return output
            elif (numbers[l]+numbers[r])<target:
                l=l+1
            else:
                r=r-1
        



