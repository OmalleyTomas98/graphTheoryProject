# Author     : Tomas O'Malley 
# Student ID : G00361128 (@gmit.ie)
# Course     : Software Development GA_KSOAG_H08 Y3
# Module     : Graph Theory  -(48901)
# Program    : NFA Builder 
# Due Date 	 : 03/04/2020

import Regex

print("**********************************************************")
print("*		                                         *")
print("* Dept- Computer Science & Applied Physics               *")
print("*         Graph Theory NFA builder        		 *")
print("*	 	                          	         *")
print("**********************************************************")

s= input("Please enter a regular expression:")

print(Regex.match("a.b|b*",s))
