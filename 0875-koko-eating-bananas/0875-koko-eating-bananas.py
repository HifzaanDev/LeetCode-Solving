class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left,right=1,max(piles)
        def can(k):
            total=0
            for p in piles:
                time=math.ceil(p/float(k))
                total=total+time
            if total<=h:
                return True
            else:
                return False
        while left<right:
            mid=(left+right)//2
            if can(mid):
                    right=mid
            else:
                left=mid+1

        return left
