class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        i=1
        maxi=0
        for i in range(len(prices)):
            if prices[i]-prices[l]<0:
                l=i
                
            maxi=max(maxi,prices[i]-prices[l])


        return maxi
        