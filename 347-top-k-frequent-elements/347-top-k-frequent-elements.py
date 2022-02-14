class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        for k,v in c.most_common(k):
            res.append(k)
        return res