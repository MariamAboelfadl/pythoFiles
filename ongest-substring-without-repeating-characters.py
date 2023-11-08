class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if(len(s)==0):
            return 0
        s=list(s)
        s.append(s[-1])
        a=[]
        m=[]
        n=0
        for i in s:
            if(i in a):
                m.append(len(a))
                a=a[a.index(i)+1:]
                a.append(i)
                
            else:
                a.append(i)
        return max(m)