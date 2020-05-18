# Author     : Tomas O'Malley
# Student ID : G00361128 (@gmit.ie)
# Course     : Software Development GA_KSOAG_H08 Y3
# Module     : Graph Theory  -(48901)
# Program    : NFA Builder
# Due Date 	 : 03/04/2020

import Regex
import argparser

print("**********************************************************")
print("*		                                         *")
print("* Dept- Computer Science & Applied Physics               *")
print("*         Graph Theory NFA builder        		 *")
print("*	 	                          	         *")
print("**********************************************************")
UserRegex= input("Please enter a regular expression: e.g  (a.b|b*) : ")
print("**********************************************************")
s= input("Please enter a single string of text: e.g bbbb :")

print("Match Result = " , Regex.match(UserRegex,s))
