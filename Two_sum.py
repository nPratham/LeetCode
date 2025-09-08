class Solution:
 #Brute Force
    ''' 
    def twoSum(self, nums,target):
        list1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    list1.append(i) 
                    list1.append(j)
        return list1
    '''
# Optimal Solution
    def twoSum(self, nums,target):
        seen={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return [seen[diff],i]
            seen[num]=i

