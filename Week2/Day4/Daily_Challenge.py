import string
import re
from collections import Counter

class Text:
    def __init__(self, text_string):
        self.text = text_string

    def _helper_tokenize(self):
        return self.text.lower().split()

    def word_frequency(self, word):
        words_list = self._helper_tokenize()
        target_word = word.lower()
        count = words_list.count(target_word)
        return count if count > 0 else f"Word '{word}' not found in text."

    def most_common_word(self):
        words_list = self._helper_tokenize()
        if not words_list:
            return "Text is empty."
        word_counts = Counter(words_list)
        return word_counts.most_common(1)[0][0]

    def unique_words(self):
        words_list = self._helper_tokenize()
        unique_set = set(words_list)
        return list(unique_set)

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
            return cls(file_content)
        except FileNotFoundError:
            print(f"Error: The file at '{file_path}' does not exist.")
            return cls("")


class TextModification(Text):
    
    def remove_punctuation(self):
        cleaned_text = re.sub(f"[{re.escape(string.punctuation)}]", "", self.text)
        return cleaned_text

    def remove_stop_words(self):
        stop_words = {
            "a", "about", "above", "after", "again", "against", "all", "am", "an", 
            "and", "any", "are", "as", "at", "be", "because", "been", "before", 
            "being", "below", "between", "both", "but", "by", "can", "did", "do", 
            "does", "doing", "don", "down", "during", "each", "few", "for", "from", 
            "further", "had", "has", "have", "having", "he", "her", "here", "hers", 
            "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", 
            "its", "itself", "just", "me", "more", "most", "my", "myself", "no", 
            "nor", "not", "now", "of", "off", "on", "once", "only", "or", "other", 
            "our", "ours", "ourselves", "out", "over", "own", "s", "same", "she", 
            "should", "so", "some", "such", "t", "than", "that", "the", "their", 
            "theirs", "them", "themselves", "then", "there", "thers", "these", 
            "they", "this", "those", "through", "to", "too", "under", "until", 
            "up", "very", "was", "we", "were", "what", "when", "where", "which", 
            "while", "who", "whom", "why", "will", "with", "you", "your", "yours", 
            "yourself", "yourselves"
        }
        
        words_list = self.text.split()
        filtered_words = [word for word in words_list if word.lower() not in stop_words]
        return " ".join(filtered_words)

    def remove_special_characters(self):
        cleaned_text = re.sub(r"[^A-Za-z0-9\s]", "", self.text)
        return cleaned_text
    


sample_string = "Bla blaa blaa bla blaaaa blaa blaaaaa"
analyzer = Text(sample_string)

print("Frequency of 'good':", analyzer.word_frequency("good"))
print("Most common word:   ", analyzer.most_common_word())
print("Unique words found: ", analyzer.unique_words()[:5])

print("\n" + "="*40 + "\n")

dirty_string = "Hello, World ! example string... special chars ($@#%)   punctuation !"
modifier = TextModification(dirty_string)

print("Original Text :            ", modifier.text)
print("No Punctuation :           ", modifier.remove_punctuation())
print("No Stop Words :            ", modifier.remove_stop_words())
print("No Special Characters :     ", modifier.remove_special_characters())