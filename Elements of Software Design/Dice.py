#  File: Dice.py
#  Description: Generate random dice rolls and create a histogram with data
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 09/11/17
#  Date Last Modified: 09/15/17

import random

def histogram(values,trials):

	height = max(values)

	if trials <= 100:

		pass

	else:

		while height >= 100:

			height = height / 10

		height = round(height)

		for index in range(len(values)):

			while round(values[index]) > height:

				num = values[index] / 10

				values[index] = round(num)

	# print y axis and data points
	for i in range(height,0,-1):

		print("|", end="")
		print(" ", end="")

		for j in range(len(values)):

			num_before = j - 1

			if values[num_before] < i or num_before < 0:

				print(" ", end="")

			if values[j] >= i:

				print("*", end ="")
				print("  ", end ="")

			else:

				print("  ", end ="")

		print()



	# print x axis and number it
	print ("+--+--+--+--+--+--+--+--+--+--+--+-")
	return ("   2  3  4  5  6  7  8  9 10 11 12")




def main():
	# keeps sequence of random numbers the same everytime
    random.seed(1314)
    # determine number of trials
    trials = int(input("How many times do you want to roll the dice? "))
    # validates trials
    while trials < 0:

    	trials = int(input("Invalid input. How many times do you want to roll the dice? "))
    				  # 2,3,4,5,6,7,8,9,10,11,12
    dice_rolls_values = [0,0,0,0,0,0,0,0,0,0,0]

    # implement dice roll trials
    for i in range(trials + 1):
    
    	dice_roll = random.randint(1,6) + random.randint(1,6)
    	# keep track of outcomes
    	index = dice_roll - 2

    	dice_rolls_values[index] = dice_rolls_values[index] + 1

    print("Results:",dice_rolls_values)
    print()

    print(histogram(dice_rolls_values,trials))

main()




