#!/usr/bin/env python3

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        def normalize(word):
            return ''.join(sorted(word.lower()))
        
        normalized_word = normalize(self.word)
        return [word for word in possible_anagrams if normalize(word) == normalized_word]
