
__author__ = "Matei Iordanescu"
__copyright__ = "Copyright (C) 2022 Matei Iordanescu"
__license__ = "mine"
__version__ = "1.0"

import random
from english_words import english_words_set
import string

# print( [char for char in string.ascii_lowercase])
english_words_list=list(english_words_set)
letters_unused=list(string.ascii_lowercase)
Hang_man_pictures=['''
   ____________
   |        |
   |        |
   |       
   |       
   |           
   |       
   |       
   |            
___|___''','''
   ____________
   |        |
   |        |
   |       ( )
   |       
   |           
   |       
   |       
   |            
___|___''','''
   ____________
   |        |
   |        |
   |       ( )
   |        |
   |           
   |       
   |       
   |            
___|___''','''
   ____________
   |        |
   |        |
   |       ( )
   |       -|
   |           
   |       
   |       
   |            
___|___''','''
   ____________
   |        |
   |        |
   |       ( )
   |       -|-
   |           
   |       
   |       
   |            
___|___''','''
   ____________
   |        |
   |        |
   |       ( )
   |       -|-
   |       /  
   |       
   |       
   |            
___|___''','''
   ____________
   |        |
   |        |
   |       ( )
   |       -|-
   |       / \    
   |
   |       
   |            
___|___''']

list_of_words=[]
myWordLength=5
for i in english_words_list:
  if len(i)<myWordLength:
    list_of_words.append(i)

hang_man_word=(random.choice(list_of_words)).lower()
# hang_man_word="teeth"
# print(hang_man_word)

List_Of_Underscors=["_"]*len(hang_man_word)

Counter_for_wrong_guesses=0
str_hang_man_word_guess=''
other_str_hang_man_word_guess=''
Mybool=True
while Mybool:
  user_input=input("Enter a letter: ").lower()
  while len(user_input)!=1:
    user_input=input("That is not 1 letter, Please enter a letter: ")

    
  while user_input not in letters_unused:
    user_input=input("You have already used that letter, Please enter a different letter: ")
  letters_unused.remove(user_input)

  if user_input not in hang_man_word:
    Counter_for_wrong_guesses=Counter_for_wrong_guesses+1
  for MyIndex,MyVal in enumerate(hang_man_word):
    if MyVal == user_input:
      List_Of_Underscors[MyIndex]=MyVal


  for i in List_Of_Underscors:
    str_hang_man_word_guess=str_hang_man_word_guess+" "+i
    other_str_hang_man_word_guess=other_str_hang_man_word_guess+i
  print(str_hang_man_word_guess)
  print(Hang_man_pictures[Counter_for_wrong_guesses])
  if Counter_for_wrong_guesses == 6:
    Mybool=False
  
  if other_str_hang_man_word_guess == hang_man_word:
    Mybool=False
  str_hang_man_word_guess=''
  other_str_hang_man_word_guess=''