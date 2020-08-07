#DaVonte' Whitfield
#ScytheSoftware TechDegree Python
#The Guessing Number Game
#Python 3.7 (64-bit)

from random import *
import os
import time

def clear():  #Note, This works with python program about not in Visual Studios, at least for me.
	os.system("cls" if os.name == "nt" else "clear")
#nt is a window check, if you are on window use cls, else clear(Mac)


def number_checker(num_test):
	if num_test < 1 or num_test > 10:
		refresh()
		print("Sorry, the rules are to guess between 1 and 10. Any other number isn't allowed, try again.")
		fixed = False #For number_checker's try and except
		while fixed != True:
			try:
				num_test = int(input("Guess a number between 1 and 10: "))
				num_test = number_checker(num_test)
				return num_test
			except:
				refresh()
				print("Sorry, letters/symbols shouldn't be entered, only numbers. Try again")
	else:
		return num_test

def game_title():
	header = "Welcome to the guessing game!"

	print(" ", "*" * len(header), '\n')
	print(" ", header.title(), '\n')
	print(" ", "*" * len(header))

def game_end():
	header = "Thanks for playing the guessing game!"

	print(" ", "-" * len(header), '\n')
	print(" ", header.title(), '\n')
	print(" ", "-" * len(header))
	print(" ", "Hope you had fun, see ya later!")

def refresh():
	clear()
	game_title()

game_title()


Random_Num = randrange(1,10) #ran command 'pip install random2' (1.0.1)
guess_attempts = 0
guess_correct = False
game_on =True
fixed = False #For try and except

while fixed != True:
	try:
		player_pick = int(input("Guess a number between 1 and 10: "))
		player_pick = number_checker(player_pick)
		fixed = True
	except:
		refresh()
		print("Sorry, letters/symbols shouldn't be entered, only numbers. Try again")

fixed = False #Resetting 'fixed'

while game_on == True:
	while (guess_correct == False):
		fixed = False #switching back to False to avoid continuous loop because of 'While fixed != True' on the try and except
		if player_pick == Random_Num:
			print("Hey, you got it!")
			guess_correct = True
		elif player_pick < Random_Num:
			refresh()
			while fixed != True:
				try:
					guess_attempts += 1
					print("Hmm, the number is Higher.")
					player_pick = int(input("Number of attempts: {} Try again: ".format(guess_attempts)))
					player_pick = number_checker(player_pick)
					fixed = True
				except:
					refresh()
					print("Sorry, letters/symbols shouldn't be entered, only numbers. Try again\n")
					guess_attempts -= 1
		elif player_pick > Random_Num:
			refresh()
			while fixed != True:
				try:
					guess_attempts += 1
					print("Hmm, the number is Lower.")
					player_pick = int(input("Number of attempts: {} Try again: ".format(guess_attempts)))
					player_pick = number_checker(player_pick)
					fixed = True
				except:
					refresh()
					print("Sorry, letters/symbols shouldn't be entered, only numbers. Try again\n")
					guess_attempts -= 1
	replay = input("Would you like to play another round? [y]es/[n]o \n>>")
	if replay.lower() == 'y':
		guess_correct = False
		guess_attempts = 0
		Random_Num = randrange(1,10) #For another round
		continue
	else:
		game_on = False
		clear()
		game_end()
time.sleep(3)
