'''class Solution:
    def groupAnagrams(self, strs):

        res = dict()
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
               

strs = ["eat","tea","tan","ate","nat","bat"]
s=Solution()
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        dect1=defaultdict(list)
        for s in strs:
            count=[0]*26
            for t in s:
                count[ord(t)-ord('a')] +=1
            key=tuple(count)
            dect1[key].append(s)
        return dect1.values()