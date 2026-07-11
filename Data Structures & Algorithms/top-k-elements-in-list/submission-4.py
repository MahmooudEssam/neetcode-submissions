class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length=len(nums)
        unique_nums=set(nums)
        length_unique=len(unique_nums)
        
        if length<1 or length>10**4 or k<1 or k>length_unique:
            return []
        hashmap={}
        for u_n in unique_nums:
            hashmap[u_n]=nums.count(u_n)
        sorted_hashmap=dict(sorted(hashmap.items(), key=lambda item:item[1],reverse=True))
        final_list=list(sorted_hashmap)
        
        return final_list[0:(k)]
        