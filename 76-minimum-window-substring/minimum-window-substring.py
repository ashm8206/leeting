class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s , len_t = len(s), len(t)

        if len_s < len_t:
            return ""

        ans = ""

        t_count =  defaultdict(int)
        
        for char in t:
            t_count[char]+=1

        
        minLen = 10**10
        
        # METHOD I - BRUTE FORCE
        
        # for i in range(len_s):

        #     s_count = defaultdict(int)

        #     for j in range(i, len_s):

        #         s_count[s[j]]+=1

        #         if all(True if char_t in s_count.keys() and s_count[char_t] >= t_count[char_t] else False for char_t in t_count.keys()):

        #             if j-i+1 < minLen:
        #                 minLen = j-i+1
        #                 ans = s[i:j+1]
        # return ans

        # O(N*2*K)

        L = 0
        have = 0
        need = len(t_count)

        s_count = defaultdict(int)

        for R in range(len_s):

            if s[R] in t_count.keys():
                s_count[s[R]]+=1
                if s_count[s[R]] == t_count[s[R]]:
                    have+=1
            
            while have == need:
                # print(s[L:R+1], s_count[s[L]], s[L], have, need)
                if R-L+1 < minLen:
                    minLen = R-L+1 
                    ans = s[L:R+1]
                
                if s[L] in t_count.keys():
                    # print(s[L], s_count[s[L]], t_count[s[L]], have)
                    s_count[s[L]]-=1
                
                    if s_count[s[L]] < t_count[s[L]]:
                        have-=1
                    # print(s[L], s_count[s[L]], t_count[s[L]], have)

                L = L+1

                # Shrink Window

        return ans





