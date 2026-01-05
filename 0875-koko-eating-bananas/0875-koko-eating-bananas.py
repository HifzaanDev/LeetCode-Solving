import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        r=max(piles)
        l=1
        k=r
        while l<=r:
            mid=(l+r)//2
            sum_of_hours_per_pile=0
            for p in piles:
                hours=math.ceil(float(p)/mid)
                sum_of_hours_per_pile=sum_of_hours_per_pile+hours
            if sum_of_hours_per_pile<=h:
                k=min(k,mid)
                r=mid-1
            elif sum_of_hours_per_pile>h:
                l=mid+1
            elif sum_of_hours_per_pile==h:
                k=min(k,mid)
                r=mid-1
                

    
        return k