from time import sleep
import random
from subprocess import call
import os
from collections import Counter



def clear():
  _ = call('clear' if os.name =='posix' else 'cls')



while True:
  option=input("\nCHOOSE...\n\n1)CHARACTERS \n2)WORDS\n\nCHOCIE: ")

  option == input

  if option == "1":
    while True:
      char=input("Enter Characters: ")
      splitc = Counter(char)
      cout=len(splitc)
      print("\nCHARACTER: ",cout)
      if char == "E":
        print("Press: E\nto Exit")
        exit()
        
        



  elif option == "2":
    while True:
      word= input("Enter words: ")
      if word == "":
        print("\nAdd atleast one word")
      elif word == "E":
        exit()
      else:
        splitw=word.split(" ")
        wout=len(splitw)
        print("Press: E\nto Exit")
        print("\nWords: ",wout)
        
    
  else:
    print("'",option,"'","is not one of the chocies.")
    sleep(2)
    clear()


  
