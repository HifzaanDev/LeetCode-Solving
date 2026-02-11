class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer=[0]*(len(temperatures))
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                answer[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return answer