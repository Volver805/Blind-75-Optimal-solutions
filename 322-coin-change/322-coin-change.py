class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        result = self.countCoins(coins, amount, 0, memo)    
        if result == math.inf:
            return -1
        return result
    def countCoins(self, coins, amount, k, memo):
        if amount < 0:
            return -1
        if amount == 0:
            return k
        if amount in memo:
            return k+memo[amount]
        x = math.inf
        for coin in coins:
            j = self.countCoins(coins, amount-coin, k+1, memo)
            if j > 0 and j < x:
                x = j
        if 0 < x:
            memo[amount] = x-k
            return x