from collections import defaultdict
import string

from server import server

class wordleBOT():

    def __init__(self, draw=False, debug=False, guess_information=False, word_information=False):
        """
        Given available letters will return guess given a file with words of the same lenght.
        Will play in hard mode.

        Yellows contains all letters known to be in the word

        draw: bool
        True No output sends results to be used with main.py
        False Writes outputs to terminal

        debug: bool
        dont use with draw
        True Outputs why words were removed.
        False No context on why letters were removed

        guess_information: bool
        will not work with draw
        True Outputs Server results from guess, if the secretWord is still in the bots words and amount of words left in the bots list

        word_information: bool
        will not work with draw
        True Gives information about remaining words and instances dictionaries

        Will hard code some values.

        TODO: Find varibles dynamically
        TODO: Ability to give different word file, not hard coded
        """

        self.source = "words.txt"
        self.words = self.loadWords()
        self.yellows = set()

        self.draw = draw
        self.debug = debug
        self.guess_information = guess_information
        self.word_information = word_information

        # Init functions
        self.instances = self.countInstances()

    def loadWords(self):
        """
        Read words from given source file. Count instances in this list, not from original
        """

        words = []

        with open(self.source, "r") as f:

            while (line:=f.readline().strip()):

                words.append(line)

        return words

    def countInstances(self):
        """
        Count instances of letters in object word list

        TODO: Review need to loop through entire list every time
        """

        instances = defaultdict(lambda: defaultdict(int))

        for word in self.words:

            for i, letter in enumerate(word):

                    instances[i][letter] += 1

        return instances

    def findWeight(self, position, letter, old_length):
        """
        Give a value to a letter based on its position where letters closer to 0.5 are weighted more.

        Current Function is 0 for 0 and 1, and 1 for 0.5 letters

        TODO: Add randomness to assigned weights
        TODO: Dissuade words with multiple of the same letter in earlier guesses
        """

        occur = self.instances[position].get(letter, 0)
        if occur == 0:
            return 0

        fraction = occur / (old_length + 1)

        if self.debug:
            print (f"{letter} : {fraction}")
            print (f"{letter} : {occur}")

        return 7 * fraction * (1 - fraction)

    def findGuess(self):
        """
        Given own list of words, loop through currently possible words
        while removing non viable words from stored list.

        Choose word with highest weight, see findWeight function
        """

        best = ""
        score = 0
        old_length = len(self.words)

        for word in self.words[:]:

            total = 0

            check = set(word).issuperset(self.yellows)

            if check:

                for i, letter in enumerate(word):

                    weight = self.findWeight(i, letter, old_length)

                    if weight == 0:

                        self.words.remove(word)

                        if self.debug:
                            print(f"{word} {letter} not in instances")

                        total = 0
                        break

                    total += weight

            else:
                self.words.remove(word)

                if self.debug:
                    print (f"{word} does not contain known letters")
                continue

            if total > score:
                best = word
                score = total

            if self.debug:
                print (f"{word} has total {total}")
                print (f"Best word is {best}")

        return best

    def updateState(self, guess, result):
        """
        Given a guess (string) and a result (list of integers) update dict of dicts by removing obsolete letters
        """

        self.instances = self.countInstances()

        for i,res in enumerate(result):
            letter = guess[i].upper()

            match res:
                case 0:
                    for j in range(5):
                        if guess[j] == letter and j != i:
                            if result[j] != 0:
                                self.instances[i].pop(letter, None)
                                break
                    else:
                        if self.debug:
                            print (f"Removed {letter}")

                        for k in range(5):

                            self.instances[k].pop(letter, None)

                case 1:
                    self.instances[i].pop(letter, None)
                    self.yellows.add(letter)
                case 2:
                    value = self.instances[i][letter]
                    self.yellows.add(letter)
                    self.instances[i] = defaultdict(int)
                    self.instances[i][letter] = value

bot = wordleBOT(guess_information=True)

### BOT TESTING BRRR ###
if not bot.draw:

    serv = server("words.txt")

    serv.getWord()
    #serv.secretWord = "UMAMI"

    print(serv.secretWord)

    guess = ""

    # TODO: Fix loop to respect wordle loops. better yet make server enforce
    for i in range(10):

        guess = bot.findGuess()
        print(f"Guess {i + 1} {guess}")

        svar = serv.checkWord(guess)

        if bot.guess_information:
            print(serv.secretWord in bot.words)
            print (len(bot.words))
            print (svar)

        if bot.word_information:
            print (bot.words)
            print (bot.instances)

        bot.updateState(guess, svar)

        if guess == serv.secretWord:
            print ("Gratulerer")
            break
