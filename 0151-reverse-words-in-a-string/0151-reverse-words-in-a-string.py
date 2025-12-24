class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        new_list=s.split()
        n=len(new_list)
        arr=[]
        for i in range(n-1,-1,-1):
            arr.append(new_list[i])
        answer=" ".join(arr)
        return answer



        