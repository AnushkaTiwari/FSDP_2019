# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:35:56 2019

@author: ANISHKA
"""

# code challenge : Weighted score calculator
# score in 3 assignments and 2 exam with max score 100 
asgn_1 = input("Enter the score in assignment 1>")
asgn_2 = input("Enter the score in assignment 2>")
asgn_3 = input("Enter the score in assignment 3>")
exam_1 = input("Enter the score in exam 1>")
exam_2 = input ("Enter the score in exam 2>")
# typecasting : converting string into integer
asgn_1 = int(asgn_1)
asgn_2 = int(asgn_2)
asgn_3 = int(asgn_3)
exam_1 = int(exam_1)
exam_2 = int(exam_2)
# total weighted score of individual 
weighted_score = ( asgn_1 + asgn_2 + asgn_3 ) * 0.1 + ( exam_1 + exam_2 ) * 0.35
print ("Total weighted score of individual")
print (weighted_score)