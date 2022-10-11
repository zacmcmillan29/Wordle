# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from platform import java_ver
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, MISSING_COLOR, PRESENT_COLOR, CORRECT_COLOR, KEY_LABELS

def wordle(): 
    # def enter_action(s):
    #     # for i in range(5): 
    #     #     gw.set_current_row(i)
    #     gw.show_message("You have to implement this method.")
    lCorrect = []
    lPresent = []
    
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




# This is where we change the keyboard colors
    def color_key(s):
        curr_row = gw.get_current_row() - 1
        # Much like the change box color function, I want to see the which letter is where and determine which color to change the keys to.
        # lCorrect = []
        # lPresent = []

        for i in range(5):
            letter = gw.get_square_letter(curr_row, i)
            letter_low = letter.lower()
            # Sets key color to the correct letter
            if (letter_low == RandWord[i]):
                CMarker = True
                for l in lCorrect:
                    if letter in l:
                        CMarker = False
                        break
                if(CMarker == True):
                    gw.set_key_color(letter, CORRECT_COLOR)
                    lCorrect.append(letter)
            else:
                # Sets key color to missing color
                marker = True
                for l in lCorrect:
                    if letter in l:
                        marker = False
                        break
                for l in lPresent:
                    if letter in l:
                        marker = False
                        break
                if(marker == True):
                    gw.set_key_color(letter, MISSING_COLOR)

        # Sets key color to Present color
        for i in range (5):
            letter = gw.get_square_letter(curr_row, i)
            letter_low = letter.lower()
            for k in range(5):
                PMarker = True
                if (RandWord[k] == letter_low):
                    PMarker = True
                    for l in lCorrect:
                        if letter in l:
                            PMarker = False
                            break
                    if(PMarker == True):
                        gw.set_key_color(letter, PRESENT_COLOR)
                        lPresent.append(letter)


    def concat_words(s):
        curr_row = gw.get_current_row()
        string = ""
        for j in range(5):
            letter = gw.get_square_letter(curr_row, j)
            string = string + letter
            string = string.lower()
        if string in FIVE_LETTER_WORDS: 
            gw.add_enter_listener(color_box)
            gw.add_enter_listener(color_key)
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
