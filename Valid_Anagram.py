class Solution(object):
    def isAnagram(self, s,t):
     '''if len(s)!=len(t):
            return False
        list1=list(t)
        for i in s:
            if i not in list1:
                return False
            list1.remove(i)
            print(list1)
        return True'''
# optimal solution
     if len(s)!=len(t):
            return False
     for i in set(s):
        if s.count(i)!=t.count(i):
            return False
        return True

