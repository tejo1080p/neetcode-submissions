class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums)
        s = [1] * len(nums)
        output = [0] * len(nums)
        n = len(nums)

        for i in range(n):
            if i == 0:
                s[n - 1] = nums[n - 1]
                for j in range(n - 2, 0, -1):
                    s[j] = s[j + 1] * nums[j]
                output[i] = s[1]
                
            elif i == n - 1:
                p[0] = nums[0]
                for j in range(1, n - 1):
                    p[j] = p[j - 1] * nums[j]
                output[i] = p[n - 2]
                
            else:
                p[0] = nums[0]
                s[n - 1] = nums[n - 1]
                
                for j in range(1, i):
                    p[j] = p[j - 1] * nums[j]
                    
                for j in range(n - 2, i, -1):
                    s[j] = s[j + 1] * nums[j]
                    
                output[i] = p[i - 1] * s[i + 1]
                
        return output
'''        p = [1] * len(nums)
        s = [1] * len(nums)
        output = [0] * len(nums)
        n = len(nums)

        for i in range(n):
            if i == 0:
                for i in range(n - 2, 0, -1):
                    s[i] = s[i + 1] * nums[i]
                    output[i] = s[i]
            elif i == n-1:
                for i in range(0,n-1):
                    p[i] = p[i+1] * nums[i]
                    output[i] = p[i]
            else:
                for i in range(1, n-1):
                    p[i] = p[i - 1] * nums[i - 1]
                for i in range(n - 2, -1, -1):
                    s[i] = s[i + 1] * nums[i + 1]
                output[i] = p[i] * s[i]
        return output'''
            

        
        