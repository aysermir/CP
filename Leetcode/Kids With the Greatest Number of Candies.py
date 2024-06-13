class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= maxNum:
                result.append(True)
            else:
                result.append(False)
        return result
        
