class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = 0
        for i in range(0, k):
            curSum += nums[i]
        maxSum = curSum
        for x in range(1, len(nums)-k+1):
            curSum = curSum - nums[x-1] + nums[x+k-1]
            if (curSum > maxSum):
                maxSum = curSum
        return maxSum/k
