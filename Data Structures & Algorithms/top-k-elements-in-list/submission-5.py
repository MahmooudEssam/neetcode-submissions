class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length=len(nums)
        unique_nums=set(nums)
        length_unique=len(unique_nums)

        if length<1 or length>10**4 or k<1 or k>length_unique:
            return []
        counts = Counter(nums)
        return [item[0] for item in counts.most_common(k)]
        