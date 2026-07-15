class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0]*26

            for char in s:
                index = ord(char)- ord('a')
                count[index] = count[index] + 1
            
            signature = tuple(count)

            if signature in groups:
                groups[signature].append(s)
            else:
                groups[signature] = [s]

        return list(groups.values())
        
        