class Solution(object):
    def isPalindrome(self, s):
        if s =='':
            return True
        newstr=''
        for i in s:
            if i.isalnum() :
                newstr += i.lower()
                print(newstr)
        for j in range(len(newstr)):
            first_pointer= newstr[j]
            second_pointer=newstr[-1-j]
            if first_pointer != second_pointer:
                return False
        return True
       

