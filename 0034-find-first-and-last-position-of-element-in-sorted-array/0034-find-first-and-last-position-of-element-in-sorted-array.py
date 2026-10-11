class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res_first=-1
        res_last=-1


        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                res_first=mid
                end=mid-1
            elif target<nums[mid]:
                end=mid-1
            else:
                start=mid+1
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                res_last=mid
                start=mid+1
                
            elif target<nums[mid]:
                end=mid-1
            else:
                start=mid+1

        return [res_first,res_last]

