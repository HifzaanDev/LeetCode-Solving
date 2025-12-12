class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        li=[]
        sumission=0
        for r in range(len(prices)):
            if prices[r]-prices[l]<0:
                l=r
            else:
                li.append(prices[r]-prices[l])
                l=r
        for ch in li:
            sumission=sumission+ch
        return sumission



