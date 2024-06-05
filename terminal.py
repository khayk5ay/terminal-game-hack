import numpy as np
import pandas as pd
import logging
from itertools import compress

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Terminal:

    def __init__(self, candidates):
        self.candidates = candidates
        print(self.candidates)
        self.n_candidates = len(candidates)
        self.len_candidates = len(candidates[0])


    def total_matches(self, first_word, second_word):
        """
        Returns the total number of letters in the 'second_word' that are in the same position in 'first_word'

            Parameters:
                first_word (str): A n letter word
                second_word (str) : A n letter word

            Returns:
                total (int) : The number of letters in the same position in both letters
        
        """
        total_matches = 0
        for i in range(len(first_word)):
            if (first_word[i] == second_word[i]):
                total_matches = total_matches + 1

        return total_matches


    def check_candidate_matches(self, main_word):
        """ For the main word, compile a list containing how many matches it has with all the words that are candidates"""
        
        matches = []
        
        for each in self.candidates:
            matches.append(self.total_matches(main_word, each))

        return matches

    def compiled(self):
        """
            Returns a dictionary of each candidate as key and the list of matches it has with the other candidates as the values
        """
        words_dict = {}

        for x, y in enumerate(self.candidates):
            words_dict[y] = self.check_candidate_matches(y)
        
        return words_dict

    
    def update_candidates(self, guess:str, clue:int):
        """
            Updates the candidate list to only show the words that that the same number of matching letters with the guess as specified in the clue

            Example:
            
            If 'vanquished' was the last guess and the game returns a clue = 2, only words that have exactly 2 matching letters will remain as candidates
        """
        words_dict = self.compiled()
        candidates_bool = list(np.array(words_dict[guess]) == clue)
        assert type(self.candidates) == list
        assert type(candidates_bool) == list
        self.candidates = list(compress(self.candidates, candidates_bool))
        

    def get_sums(self):
        sum_dict = {}
        words_dict = self.compiled()
        for each in words_dict.keys():
            sum_dict[each] = sum(words_dict[each])

        return sum_dict

        
    def most_likely(self):
        """
            Returns the most likely candidate(s) that the user can pick a guess from
        """
        likely = []
        sum_dict = self.get_sums()
        highest_chance = max(sum_dict.values())

        for candidate, total in sum_dict.items():
            if total == highest_chance:
                likely.append(candidate)

        print(likely)

        return
    
      

        
