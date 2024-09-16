class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        lettermap = {
            1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'],0:[]
        }
        res = []
        if not digits:
            return res
        def backtrack(comb,next_d):
            if not next_d:
                res.append(comb)
            else:
                for letter in lettermap[int(next_d[0])]:
                    backtrack(comb+letter,next_d[1:])
        
        backtrack("",digits)
        return res