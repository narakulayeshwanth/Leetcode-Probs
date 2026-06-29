class WordFilter:

    def __init__(self, words: List[str]):
        self.mp = {}
        for index, word in enumerate(words):
            n = len(word)
            for i in range( n + 1):
                prefix = word[:i]
                for j in range( n + 1):
                    suffix = word[j:]
                    self.mp[(prefix, suffix)] = index
    def f(self, pref: str, suff: str) -> int:
        return self.mp.get((pref, suff), -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)