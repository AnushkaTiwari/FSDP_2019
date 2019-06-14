# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:17:42 2019

@author: ANISHKA
"""

# code challenge : Anagram

def Anagram_check(word1 , word2):
    if (len(word1)==len(word2)):
        if (sorted(word1)==sorted(word2)):
           return True
        else:
           return False
    else:
        return False
       
        
        
first_word=input("Enter the first word:")
second_word=input("Enter the second word:")

print(Anagram_check(first_word , second_word))