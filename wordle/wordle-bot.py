from collections import defaultdict
import string

class wordleBOT():

    def __init__(self):
        """
        Given available letters will return guess given a file with words of the same lenght.
        Will play in hard mode. So it must use green letters in said place and guess must contain all yellows

        Will hard code some values.
        TODO: Find varibles dynamically
        TODO: Ability to give different word file, not hard coded
        """

        self.validLetters= string.ascii_uppercase
        self.totalWords = 12915
        self.source = "words.txt"
        self.knowledge = 5 * [""]

        # Init functions
        self.instances = self.countInstances()

    def countInstances(self):
        """
        Given list of words that are the same length, make a dictionary of dictionaries holding the occurance of each letter in each position.
        """

        instances = defaultdict(lambda: defaultdict(int))

        with open(self.source, "rb") as f:

            #Read until empty string (EOF) is passed
            while (line := f.readline()):

                for i, letter in enumerate(line.strip()):

                    instances[i][chr(letter)] += 1

        return instances

    def findGuess(self):
        """
        Given valid letters finds best word based of formula for calculating based of letter frequency.

        TODO: Logic for handling valid letters. I think regex will let me do what i want. Ask Isak.
        """

        None

    def updateState(self, guess, result):
        """
        Given a guess (string) and result (list with integers) update validLetters string, update correct letters and yellow letters

        Remove letters from yellows if it becomes green
        """

        for i,res in enumerate(result):
            letter = guess[i].upper()

            match res:
                case 0:
                    self.validLetters = self.validLetters.replace(letter, '')
                case 1:
                    # undersøk om dette er nok logikk
                    if letter not in self.knowledge:
                        #self.yellows.append(letter)
                case 2:
                    self.knowledge[i] = letter
                    if letter in self.yellows:
                        #self.yellows.remove(letter)

        print (self.validLetters)
        print (self.knowledge)


bot = wordleBOT()
#print (bot.knowledge)

# This does not work quite correct
bot.yellows = ["O"]
bot.updateState("MOoDI", [0,2,1,0,0])
