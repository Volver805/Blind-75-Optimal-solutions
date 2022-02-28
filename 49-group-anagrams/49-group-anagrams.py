class Solution:
    def groupAnagrams(self, strs: List[str]):
        occur = []
        res = []
        for string in strs:
            t = {}
            for ch in string:
                t[ch] = t.get(ch, 0) + 1
            self.appendGroup(res, occur, t, string)
        return res

                    
    def appendGroup(self, res:list, occur:list, t:dict, string:str):
        for i in range(len(occur)):
            if occur[i] == t:
                res[i].append(string)
                return
        occur.append(t)
        res.append([string])