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

        self.source = "words.txt"
        self.words = self.loadWords()

        # Hacky solution since words being removed dont immidiatly change instances such that certain letters will get negative weight
        self.old_length = 0

        # List of letters that are in the word but not a green letter i.e. position is unknow
        self.yellows = set()

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

    def findWeight(self, position, letter):
        """
        Give a value to a letter based on its position where letters closer to 0.5 are weighted more.

        Current Function is 0 for 0 and 1, and 1 for 0.5 letters

        TODO: Add randomness to assigned weights
        TODO: Dissuade words with multiple of the same letter in earlier guesses
        """

        occur = self.instances[position].get(letter, 0)
        if occur == 0:
            return 0

        fraction = occur / (self.old_length + 1)
        #print (len(self.words))
        #print (f"{letter} : {fraction}")
        #print (f"{letter} : {occur}")
        #print (1 - fraction**2)

        return 7 * fraction * (1 - fraction)

    def findGuess(self):
        """
        Given own list of words, loop through currently possible words
        while removing non viable words from stored list.

        Choose word with highest weight, see findWeight function
        """

        best = ""
        score = 0
        self.old_length = len(self.words)

        for word in self.words[:]:

            total = 0

            check = set(word).issuperset(self.yellows)
            #print (check)

            if check:

                for i, letter in enumerate(word):

                    weight = self.findWeight(i, letter)

                    if weight == 0:

                        self.words.remove(word)
                        #print(f"{word} letter not in word")

                        total = 0
                        break

                    total += weight

            else:
                self.words.remove(word)
                #print (f"{word} does not contain known letters")
                continue

            if total > score:
                best = word
                score = total
                #print (best)

            #print (f"{word} has total {total}")
            #print (f"Best word is {best}")

        #print (counter)

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
                        for k in range(5):
                            #print (f"fjerna nå {letter}")
                            self.instances[k].pop(letter, None)

                case 1:
                    self.instances[i].pop(letter, None)
                    self.yellows.add(letter)
                case 2:
                    value = self.instances[i][letter]
                    self.yellows.add(letter)
                    self.instances[i] = defaultdict(int)
                    self.instances[i][letter] = value

bot = wordleBOT()

### BOT TESTING BRRR ###
#serv = server("words.txt")
#serv.getWord()
##serv.secretWord = "UMAMI"
#print(serv.secretWord)
#
#guess = ""
#
#for i in range(10):
#
    #guess = bot.findGuess()
    #print(f"Guess {i + 1} {guess}")
    ##print(serv.secretWord in bot.words)
    #print (len(bot.words))
    ##print (bot.words)
    ##print (bot.instances)
#
    #svar = serv.checkWord(guess)
    #bot.updateState(guess, svar)
    #print (svar)
#
    #if guess == serv.secretWord:
        #print ("Gratulerer")
        #break
