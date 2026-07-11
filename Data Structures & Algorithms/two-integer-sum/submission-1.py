class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        if length>1000 or length<2 or target>10000000 or target<-10000000: #To check contraints
            return [] 
        seen={} #hash map to contain previous seen values
        for i, n in enumerate(nums):
            diff= target - n
            if diff in seen:
                return [seen[diff],i]
            seen[n]=i
        return
        