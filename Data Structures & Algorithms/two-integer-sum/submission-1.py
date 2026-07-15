class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [seen[comp],i]
            else:
                seen[nums[i]] = i
'''            i =0
            j = i+1
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]
                    else:
                        i + 1 == i'''
        
        