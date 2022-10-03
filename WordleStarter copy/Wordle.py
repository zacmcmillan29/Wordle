# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle(): 
    # def enter_action(s):
    #     # for i in range(5): 
    #     #     gw.set_current_row(i)
    #     gw.show_message("You have to implement this method.")
    
    def word_not_found(s):
        gw.show_message("This is not a word. Please enter a valid word.")
    
# Iterate over each row and then each column. Create a string from each letter. Add each letter to the previously created word.
    def concat_words(s):
        for i in range(5):
            for j in range(5):
                string = " "
                letter = gw.get_square_letter(i, j)
                string = string + letter
                # string = f"{string}{letter}" 
                # this is just to test if the concatenation works
                gw.show_message("The word is: " + string) 
# this part checks if word is valid and if not, display proper message, if so, add one to current row.
        string = ""
        for words in FIVE_LETTER_WORDS: 
            if string != words: 
                gw.add_enter_listener(word_not_found)  
                gw.set_current_row(2)
            # add 1 to the current_set_row to make next guess on the next row if word is found
            else: 
                # need to create method to add one to row 
                gw.set_current_row(1)            
            

# check if string is in the dictionary. if not, display message. If so, add one to current row.            
    def check_word(s): 
        string = ""
        gw.set_current_row(0)
        for words in FIVE_LETTER_WORDS: 
            if string != words: 
                gw.add_enter_listener(word_not_found)  
                gw.set_current_row(2)
            # add 1 to the current_set_row to make next guess on the next row if word is found
            else: 
                gw.set_current_row(1)

                       
    gw = WordleGWindow()    
    gw.add_enter_listener(concat_words)
    gw.add_enter_listener(check_word)
    # gw.add_enter_listener(enter_action)
    
       
    RandWord = FIVE_LETTER_WORDS[random.randrange(0,len(FIVE_LETTER_WORDS),1)]
    print(RandWord)
    for i in range(5):
        gw.set_square_letter(0, i, RandWord[i])

# Startup code

if __name__ == "__main__":
    wordle()


