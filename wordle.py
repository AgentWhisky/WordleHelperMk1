from english_words import english_words_set


class wordle:
    def __init__(self):
        self.wordLength = 5

        # Build Master Word List
        self.master_word_list = []
        self._getWords()

    # yesLetters is a list confirmed letters
    # noLetters is a list() of denied letters
    # setWord is the set word with specific letter locations or *
    def possibleWords(self, yesLetters, noLetters, setWord):
        words = []
        for word in self.master_word_list:
            if self._setWordCheck(word, setWord):  # Check SetWord
                if self._yesLettersCheck(word, yesLetters):
                    if self._noLettersCheck(word, noLetters):
                        words.append(word)

        return words

    # Private Functions
    def _getWords(self):
        for word in english_words_set:
            if len(word) == self.wordLength:
                self.master_word_list.append(word.upper())

    def _setWordCheck(self, word, setWord):
        for i in range(self.wordLength):
            if not setWord[i] == '*':
                if word[i] != setWord[i]:
                    return False
        return True

    def _yesLettersCheck(self, word, yesLetters):
        for letter in yesLetters:
            if not letter in word:
                return False
        return True

    def _noLettersCheck(self, word, noLetters):
        for letter in noLetters:
            if letter in word:
                return False
        return True


def main():
    w = wordle()

    yesLetters = ['A', 'E', 'T']
    noLetters = ['P', 'L', 'G', 'M', 'S', 'N', 'V', 'H', 'C', 'D']
    setWord = ['*', 'A', '*', 'E', '*']

    possible = w.possibleWords(yesLetters, noLetters, setWord)
    print(possible)


if __name__ == "__main__":
    main()
