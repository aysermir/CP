class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = len(digits) - 1
        if digits[x]!=9:
            digits[x]+=1
            return digits
        for i in range(x,-1,-1):
            if i == 0 and digits[i] == 9:
                digits[i]=0
                digits = [1]+digits
                return digits
            if digits[i] == 9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
