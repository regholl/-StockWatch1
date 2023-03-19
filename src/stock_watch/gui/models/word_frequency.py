class WordFrequency(object):
    def __init__(self, words: list=None):
        # Create a dictionary count of words
        self.filtered_filler_words = ["to", "of", "the", "in", "as", "for", "and", "on", "a", "is", "oh", "um", "uh",
                                      "er", "ah", "like", "well", "so", "right", "literally", "okay", "very", "really",
                                      "actually", "basically", "definitely", "literally", "just", "totally",
                                      "seriously", "`", "~", "=", "+", "-", "_", "!", "@", "#", "$", "%", "^", "&", "*",
                                      "(", ")", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', ",", "<", ".", ">",
                                      "/", "?", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us",
                                      "them", "my", "your", "his", "her", "its", "our", "their", "mine", "yours",
                                      "hers", "ours", "theirs", "am", "is", "are", "was", "were", "be", "been", "being",
                                      "have", "has", "had", "do", "does", "did", "can", "could", "may", "might", "must",
                                      "will", "would", "shall", "should", "a", "an", "the", "and", "but", "or", "if",
                                      "then", "else", "when", "at", "from", "by", "on", "off", "for", "in", "out",
                                      "over", "to", "into", "with", "without", "about", "above", "below", "between",
                                      "under", "until", "while", "where", "why", "how", "all", "any", "both", "each",
                                      "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
                                      "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
                                      "should", "now", "i", "after", "this", "that", "these", "those", "what", "which",
                                      "here", "there", "where", "who", "whom", "whose", "when", "why", "how", "also",
                                      "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                                      "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                                      "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty",
                                      "seventy", "eighty", "ninety", "hundred", "thousand", "million", "billion",
                                      "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "up", "say",
                                      "back", "get", "go", "make", "know", "take", "see", "come", "think", "look"
                                      "want", "give", "use", "find", "tell", "ask", "work", "seem", "feel", "try",
                                      "leave", "call", "good", "new", "first", "last", "long", "great", "little",
                                      "own", "other", "old", "right", "big", "high", "different", "small", "large",
                                      "next", "early", "young", "few", "bad", "same", "able",
                                      "to", "of", "in", "for", "on", "with", "at", "by", "from", "up", "about", "into"
                                      "over", "after", "under", "above", "the", "and", "a", "that", "I",
                                      "it", "not", "he", "as", "you", "this", "but", "his", "they", "her", "she",
                                      "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
                                      "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when",
                                      "make", "can", "like", "time", "no", "just", "him", "know", "take", "says"]
        self.word_frequency = {}
        if words is not None:
            self.add_words(words)

    def add_words(self, words: list):
        # normalize the words
        words = [word.lower() for word in words]

        # Add words to the dictionary if not in filtered_filler_words
        for word in words:
            if word not in self.filtered_filler_words:
                if word in self.word_frequency:
                    self.word_frequency[word] += 1
                else:
                    self.word_frequency[word] = 1

    def get_frequency(self, word: str):
        # Return the frequency of a word
        return self.word_frequency[word]

    def get_most_frequent(self, n: int):
        # Return the n most frequent words
        return sorted(self.word_frequency, key=self.word_frequency.get, reverse=True)[:n]