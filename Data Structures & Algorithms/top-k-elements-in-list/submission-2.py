class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] = seen[i] + 1
            else:
                seen[i] = 1


        buckets = [[] for _ in range(len(nums)+1)]

        for num,freq in seen.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        
'''sorted_seen = dict(sorted(seen.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_seen.keys())[:k]'''
