#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:38:56 2022

"""

import random #importing random to be used later in code

print("Welcome to the game of sticks!") 


sticksLeft = int(input("How many sticks are on the table initially (10-100)?")) #getting initial input for number of sticks used in game
sticksPicked= 0
player1 = True                                                                  #defining player1's turn
print("There are {} sticks on the table.".format(sticksLeft))




while sticksLeft > 0:
    while player1 == True and sticksLeft > 0 :

        sticksPicked = int(input("How many sticks do you want to pick up (1-3)?"))
                                                                                #if,elif and else loop used to set restrictions to the number of sticks the player is allowed to pick up.
        if sticksPicked > 3:
            print( "You can't remove more than three sticks at a time! There are" + str(sticksLeft) + "sticks on the table.")     
        elif sticksLeft - sticksPicked < 0:
            print("Not enough sticks left")                                  
        else:
            sticksLeft -= sticksPicked
            print( "You picked up " + str(sticksPicked) + 
                " sticks. There are " + str(sticksLeft) + " sticks on the table.")    

            player1 = False                       

    while player1 == False and sticksLeft > 0:                                  # while loop for when its is not player 1's turn and sticksLeft >0 

        computer = random.randint( 1, min(3, sticksLeft) )                      #making sure that computer selects a number between 1-3 and less than the sticksLeft on the table.
        sticksLeft -= computer                                                  #using random function generate rendom number from import above and min function to return lowest value with parameters 3 and remaining sticks.

        print( "Computer selects " + str(computer) + 
            " sticks. There are " + str(sticksLeft) +" sticks on the table")    

        player1 = True 

if player1 == True:
    print("The computer took the last stick,You won the game!")
else:
   print("You took the stick, the computer wins !")                             #else condition where it is player 1's turn and the last stick is on the table to prompt player lost the game.
