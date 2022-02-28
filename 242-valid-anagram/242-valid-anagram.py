class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ¯\_(ツ)_/¯
        # return sorted(s) == sorted(t)
        characters, target = {}, {}
        for ch in s:
            characters[ch] = characters.get(ch, 0) + 1
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        return characters == target
            