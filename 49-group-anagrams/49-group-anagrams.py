class Solution:
    def groupAnagrams(self, strs: List[str]):
        res = defaultdict(list)
        for string in strs:
            counter = [0] * 26
            for ch in string:
                counter[ord(ch) - ord('a')] += 1
            res[tuple(counter)].append(string)
        return res.values()