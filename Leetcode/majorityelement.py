class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        maxx = max(hashmap.values())
        for key, value in hashmap.items():
            if maxx == value:
                return key
