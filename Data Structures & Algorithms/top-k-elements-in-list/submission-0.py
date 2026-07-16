class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] = seen[i] + 1
            else:
                seen[i] = 1
                
        # Sorted dictionary by frequency values in descending order
        sorted_seen = dict(sorted(seen.items(), key=lambda x: x, reverse=True))
        
        # Get the keys as a list and slice the first k elements
        return list(sorted_seen.keys())[:k]
