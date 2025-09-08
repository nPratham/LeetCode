class Solution(object):
    def productExceptSelf(self, nums):
        list1=[]
        for i in range(len(nums)):
            prefix= nums[:i] 
            suffix=nums[i+1:]
            new_list= prefix+suffix
            value=1
            for j in new_list:
                value*=j
            list1.append(value)
        return list1
        