from collections import defaultdict
import string

from server import server

class wordleBOT():

    def __init__(self):
        """
        Given available letters will return guess given a file with words of the same lenght.
        Will play in hard mode.

        Will hard code some values.
        TODO: Find varibles dynamically
        TODO: Ability to give different word file, not hard coded
        """


        self.words=[]
        self.source = "words.txt"

        # Init functions
        self.instances = self.countInstances()

    def countInstances(self):
        """
        Given list of words that are the same length, make a dictionary of dictionaries holding the occurance of each letter in each position.

        Appends words to words list
        """

        instances = defaultdict(lambda: defaultdict(int))

        with open(self.source, "rb") as f:

            #Read until empty string (EOF) is passed
            while (line := f.readline()):

                self.words.append(line.decode().strip())

                for i, letter in enumerate(line.strip()):

                    instances[i][chr(letter)] += 1

        return instances

    def findWeight(self, position, letter):
        """
        Give a value to a letter based on its position where letters closer to 0.5 are weighted more.

        Current Function is 0 for 0 and 1, and 1 for 0.5 letters

        TODO: Optimize for betters guesses?
        TODO: Add randomness to assigned weights
        TODO: Dissuade words with multiple of the same letter in earlier guesses
        """

        #if self.instances[position].has_key(
        occur = self.instances[position].get(letter, 0)
        fraction = occur / len(self.words)

        return 7 * fraction * (1- fraction)

    def findGuess(self):
        """
        Given own list of words, loop through currently possible words
        while removing non viable words from stored list.

        Choose word with highest weight, see findWeight function
        """

        best = ""
        score = 0

        for word in self.words:

            total = 0

            for i, letter in enumerate(word):

                total += self.findWeight(i, letter)

            if total > score:
                best = word
                score = total

        return best

    def updateState(self, guess, result):
        """
        Given a guess (string) and a result (list of integers) update dict of dicts by removing obsolete letters
        """

        for i,res in enumerate(result):
            letter = guess[i].upper()

            match res:
                case 0:
                    for j in range (0, 5):

                        # Perhaps Inefficient, but it works
                        if len(self.instances[j]) != 1:
                            self.instances[j].pop(letter, None)
                case 1:
                    self.instances[i].pop(letter, None)
                case 2:
                    value = self.instances[i][letter]
                    self.instances[i] = defaultdict(int)
                    self.instances[i][letter] = value

            #print (self.instances[i])


bot = wordleBOT()
#bot.updateState("HELLO", [2,1,2,0,0])

### BOT TESTING BRRR ###
serv = server("words.txt")
serv.getWord()
print(serv.secretWord)

guess = ""

for i in range(10):

    guess = bot.findGuess()
    print(guess)

    svar = serv.checkWord(guess)
    bot.updateState(guess, svar)

    if guess == serv.secretWord:
        print ("Gratulerer")
        break
