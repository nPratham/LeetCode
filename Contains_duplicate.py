class Solution(object):
    def containsDuplicate(self, nums):
        if nums ==[]:
            return False
        distinct_element=set()
        for i in nums:
            if i not in distinct_element:
                distinct_element.add(i)
            else:
                return True
        return False
    
