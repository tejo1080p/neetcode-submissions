class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        c_map = {}
        for c in s:
            if c in c_map:
                c_map[c] = c_map[c] + 1
            else:
                c_map[c] = 1

        for c in t:
            if c not in c_map:
                return False
            
            c_map[c] = c_map[c] - 1

            if c_map[c] < 0:
                return False
        
        return True
        

    '''    s_map = {}
        t_map = {}
        for i in s: 
            if i in s_map:
                s_map[i] = s_map[i] + 1
            else:
                s_map[i] = 1

        for j in t:
            if j in t_map:
                t_map[j] = t_map[j] + 1
            else:
                t_map[j] = 1


        return s_map == t_map '''
