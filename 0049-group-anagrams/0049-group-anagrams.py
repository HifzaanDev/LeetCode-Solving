class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen={}
        arr=[]
        final=[]
        for ch in strs:
            arr=[]
            n=len(ch)
            for i in range (n):
                arr.append(ch[i])
            arr.sort()
            sorted_string="".join(arr)
            if sorted_string in seen:
                seen[sorted_string].append(ch)
            else:
                seen[sorted_string]=[]
                seen[sorted_string].append(ch)

        for cha in seen:
            final.append(seen[cha])
        return final
            



            
            
