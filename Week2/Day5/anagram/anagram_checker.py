class AnagramChecker :
    def __init__(self, file_path) :
        try :
            with open(file_path, "r", encoding="utf-8") as file :
                self.word_list = {word.strip().lower() for word in file.read().split()}
        except FileNotFoundError :
            self.word_list = set()

    def is_valid_word(self, word) :
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2) :
        w1, w2 = word1.lower(), word2.lower()
        if w1 == w2 :
            return False
        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word) :
        anagrams = []
        for dictionary_word in self.word_list :
            if self.is_anagram(word, dictionary_word) :
                anagrams.append(dictionary_word)
        return anagrams