import os
import random as r
import string

class server():
    """
    Class that returns new wordle word from source.

    Takes guess and returns answers.
    """

    def __init__(self, source):
        """
        Initialize with source file (assuming ascii encoding)
        Find size of file in bytes.

        Set secret word as empty string. Populated by running getWord

        TODO: Adapt sourcing to variable encoding
        """

        self.source = source
        self.length = 5
        self.offset = 6
        self.amountWords = os.path.getsize(source) / self.offset

        self.secretWord = ""

    def getWord(self):
        """
        Sets self.secretWord to random word from source list.
        Set as a list with self.length elements.

        Not validated.
        """

        tall = r.randint(0, self.amountWords)
        word = ""

        with open(self.source, "rb+") as f:

            # move to nth line
            f.seek(tall * self.offset)

            # read and decode
            word = f.read(self.length).decode("ascii")

        self.secretWord = [x for x in word]

    def checkWord(self, word):
        """
        Checks given word against chosen secret word.

        Returns list with 0, 1 or 2.

        0 - Letter is not in the word.
        1 - Letter is in the wrong place.
        2 - Letter is in the right place.
        """

        # TODO: Ikke tillate tidligere gjett

        wordList = [x.upper() for x in word]

        for i,letter in enumerate(self.secretWord):
            if letter == wordList[i]:
                # skriver om input slik at bokstav ikke tolkes flere ganger
                wordList[i] = 2

        for i, letter in enumerate(wordList):
            # LK stygt men funker
            if letter == 2:
                continue

            try:
                index = self.secretWord.index(letter)
                wordList[i] = 1

            except:
                wordList[i] = 0

        return wordList


    def remainingLetters(self, attempt):

        """
        Return list of letters that have already been used

        TODO: Write function remainingLetters
        """
        alphabet = string.ascii_uppercase

        attempt = set(attempt)

        for char in alphabet_set:
            alphabet.replace(char, "")

        print (alphabet)

#ser = server("words.txt")
#
## pick random word
#tall = r.randint(0, ser.amountWords)
#ser.getWord(tall)
#
#print(ser.secretWord)
#print(ser.checkWord("hello"))
