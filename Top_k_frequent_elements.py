class Solution(object):
    def topKFrequent(self, nums, k):
        frequency_of_elements={}
        for i in nums:
            if i in frequency_of_elements:
                frequency_of_elements[i]+=1
            else:
                frequency_of_elements[i]=1
            
        list1=list(frequency_of_elements.items())
        list1.sort(key=lambda x:x[1],reverse=True)
        new_list=[]
        for j in range(k):
            new_list.append(list1[j][0])
        return new_list
        