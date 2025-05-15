from collections import defaultdict
import string

class wordleBOT(source):

    def __init__(self):
        """
        Given available letters will return guess given a file with words of the same lenght.

        Will hard code some values.
        TODO: Find varibles dynamically
        TODO: Ability to give different word file, not hard coded
        """

        self.valid_letters = string.ascii_uppercase
        self.total_words = 12915
        self.source = "words.txt"

        # Init functions
        self.instances = self.countInstances(self.source)

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
