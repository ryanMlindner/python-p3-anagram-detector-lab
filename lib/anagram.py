# your code goes here!
class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, list):
        anagrams = []
        compare = sorted([letter for letter in self.word])
        for word in list:
            sorted_word = sorted([letter for letter in word])
            if (compare == sorted_word):
                anagrams.append(word)
        return anagrams
