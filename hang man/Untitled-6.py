# step1
word_list = ["aardvark", "baboon", "camel"]

#TODO_1 - randomly chose a word from the word_list and assignd it to a variable called chossen_word.

import random

chosen_word = random.choice(word_list)

#TODO_2 Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.

guess = input("guess a letter : ")

Cguess = guess .lower()

#TODO_3 check if the letter the user guessed (guess) is one of the letters in the chosen_word.
new_word = []

blank_space = []

new_word = list(chosen_word)

for i in new_word:
    if i == Cguess:
        blank_space += Cguess
    else:
        blank_space += '_'

print(blank_space)




#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#new_wordList = []


#for i in word_list:
#    new_wordList.append(new_word)
#    

#print(new_wordList)
