# step1
word_list = ["aardvark", "baboon", "camel"]



import random

chosen_word = random.choice(word_list)


new_word = []

blank_space = []

new_word = list(chosen_word)








while blank_space != new_word:
    guess = input("guess a letter : ")
    Cguess = guess .lower()
    for i in new_word:
        if i == Cguess:
            blank_space = Cguess
        else:
            blank_space += '_'
            if 
    print(blank_space)