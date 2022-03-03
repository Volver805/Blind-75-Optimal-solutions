class WordDictionary:

    def __init__(self, word = False):
        self.word = word
        self.children = {}

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.word = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = WordDictionary()
        self.children[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:        
        if len(word) == 0:
            return self.word
        if word[0] == '.':
            for child in self.children.values():
                if child.search(word[1:]):
                    return True
            return False
        if word[0] not in self.children:
            return False
        return self.children[word[0]].search(word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)