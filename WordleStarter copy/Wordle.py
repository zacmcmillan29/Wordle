# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from platform import java_ver
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, MISSING_COLOR, PRESENT_COLOR, CORRECT_COLOR

def wordle(): 
    # def enter_action(s):
    #     # for i in range(5): 
    #     #     gw.set_current_row(i)
    #     gw.show_message("You have to implement this method.")
    
    def word_not_found(s):
        gw.show_message("This is not a word. Please enter a valid word.")
        
    def word_found(s):
        gw.show_message("This is a valid word.")
    
# Iterate over each row and then each column. Create a string from each letter. Add each letter to the previously created word.
    def color_box(s):
        curr_row = gw.get_current_row() - 1
        for i in range(5):
            letter = gw.get_square_letter(curr_row, i).lower()
            if (letter == RandWord[i]):
                gw.set_square_color(curr_row,i, CORRECT_COLOR)
            else:
                gw.set_square_color(curr_row, i, MISSING_COLOR)
        for i in range (5):
            letter = gw.get_square_letter(curr_row, i).lower()
            for k in range(5):
                if (RandWord[k] == letter and gw.get_square_color(curr_row, k)!= CORRECT_COLOR):
                    gw.set_square_color(curr_row,i, PRESENT_COLOR)




    def concat_words(s):
        curr_row = gw.get_current_row()
        string = ""
        for j in range(5):
            letter = gw.get_square_letter(curr_row, j)
            string = string + letter
            string = string.lower()
        if string in FIVE_LETTER_WORDS: 
            gw.add_enter_listener(color_box)
            gw.add_enter_listener(word_found)
            
            gw.set_current_row(gw.get_current_row() + 1)
        else: 
            gw.add_enter_listener(word_not_found)
            

    


    
                       
    gw = WordleGWindow()    

    RandWord = FIVE_LETTER_WORDS[random.randrange(0,len(FIVE_LETTER_WORDS),1)]
    
    #*********Zach - Comment Out Next Three lines to hide correct word
    print(RandWord)
    for i in range(5):
        gw.set_square_letter(0, i, RandWord[i])




    #gw.add_enter_listener(color_box)
    gw.add_enter_listener(concat_words)
    
    
       
    

    
    

# Startup code

if __name__ == "__main__":
    wordle()
