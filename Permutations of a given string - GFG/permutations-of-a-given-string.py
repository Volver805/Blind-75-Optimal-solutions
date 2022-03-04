#User function Template for python3

class Solution:
    def find_permutation(self, S):
        permutations, res = self.getAllPermutations(S), []
        for permutation in permutations:
            if len(permutation) == len(S):
                res.append((permutation))
        return sorted(res)


    def getAllPermutations(self, word):
        if len(word) == 1:
            return [word]
        letter = word[0]
        permutations = self.getAllPermutations(word[1:])
        for permutationIndex in range(len(permutations)):
            for i in range(len(permutations[permutationIndex])+1):
                permutations.append(permutations[permutationIndex][:i] + letter + permutations[permutationIndex][i:])
        return permutations

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends