class Solution(object):
    def twoSum(self, numbers, target):
        first_pointer=0
        n=len(numbers)
        second_pointer=n-1
        
        while first_pointer<second_pointer:   
            if numbers[first_pointer]+numbers[second_pointer]==target:
                return[first_pointer+1,second_pointer+1]
            elif numbers[first_pointer]+numbers[second_pointer]>target:
                second_pointer-=1
            else:
                first_pointer+=1




