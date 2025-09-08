class Solution(object):
    def findClosestNumber(self, nums):
        min_value=nums[0]
        for i in range(1,len(nums)): 
            if min_value <0:
                minimum = -min_value
            else:
                minimum= min_value 
            if nums[i]<0:
                current=-nums[i]
            else:
                current=nums[i]
            if current<minimum:
                min_value=nums[i]
            elif current == minimum:
                if nums[i]>min_value:
                    min_value=nums[i]
        return min_value
