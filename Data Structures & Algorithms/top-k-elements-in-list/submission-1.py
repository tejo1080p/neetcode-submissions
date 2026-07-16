class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] = seen[i] + 1
            else:
                seen[i] = 1
                
        
        sorted_seen = dict(sorted(seen.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_seen.keys())[:k]
