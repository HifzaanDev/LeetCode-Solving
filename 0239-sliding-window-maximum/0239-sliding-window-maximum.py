class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        i=j=0
        res=[]
        if k==0:
            return res

        q=collections.deque()
        for j in range (len(nums)):
            while q and nums[j]>nums[q[-1]]:
                q.pop()
            
            if q and q[0]<i:
                q.popleft()

            q.append(j)

            if j-i+1==k:
                res.append(nums[q[0]])
                i=i+1
        return res