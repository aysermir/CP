class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        # This imo is an easier solution but only works because of python
        #return num == num[::-1]
        x = len(num)-1
        for i in range(len(num)//2):
            if num[i]!=num[x]:
                return False
            x=x-1
        return True

        
