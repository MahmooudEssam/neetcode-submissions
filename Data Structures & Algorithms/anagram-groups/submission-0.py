class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length=len(strs)
        if length<1 or length>1000:
            return []
        seen={}
        for word in strs:
            key=''.join(sorted(word))
            seen.setdefault(key, []).append(word)
        print (seen)
        return list(seen.values())

        