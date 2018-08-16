#  File: sorting.py
#  Description: sorting
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 12/01/17
#  Date Last Modified: 12/01/17

import random
import time
import sys
sys.setrecursionlimit(10000)

# sorting methods
def bubbleSort(alist):
	for passnum in range(len(alist)-1, 0, -1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

def insertionSort(alist):
	for index in range(1, len(alist)):
		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position-1] > currentvalue:
			alist[position] = alist[position-1]
			position = position-1

		alist[position] = currentvalue

def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist) // 2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf):
			alist[k] = righthalf[j]
			j += 1
			k += 1

def quickSort(alist):
	quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist,first,last):
	if first < last:
		splitpoint = partition(alist, first, last)
		quickSortHelper(alist, first, splitpoint-1)
		quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
	pivotvalue = alist[first]
	leftmark = first+1
	rightmark = last
	done = False

	while not done:

		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark += 1
		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark -= 1

		if rightmark < leftmark:
			done = True
		else: 
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark


# counts time
# returns elapsed time
def functionTimer(sortFunc, *args):

	startTime = time.time()
	sortFunc(*args)
	endTime = time.time()
	elapsedTime = endTime - startTime

	return elapsedTime

# turn list into almost sorted
def almostSorted(alist):

	for i in range(len(alist)):
		r_idx = random.randint(0, len(alist)-1)
		r_idx2 = random.randint(0, len(alist)-1)

		alist[r_idx], alist[r_idx2] = alist[r_idx2], alist[r_idx]

def main():

	# create lists with 10, 100, 1000 ints
	myList = [i for i in range(10)]
	myList2 = [i for i in range(100)]
	myList3 = [i for i in range(1000)]

	sortMethods = [bubbleSort, insertionSort, mergeSort, quickSort]
	strings = ["bubbleSort", "insertionSort", "mergeSort", "quickSort"]
	list_type = ["Random", "Sorted", "Reverse", "Almost sorted"]

	for h in range(4):

		# prints heads for each type of list
		print("Input type =", list_type[h])
		print("                    avg time    avg time    avg time")
		print("   Sort function     (n=10)      (n=100)    (n=1000)")
		print("--------------------------------------------------------")

		for i in range(4):
			# prints sorting method being used
			print("{:>16}".format(strings[i]), end = "")

			# starts timer for each of the 3 different length list
			time = 0
			time2 = 0
			time3 = 0

			# do sort methods 5 times
			# to calculate avg
			for j in range(5):

				# shuffles a list 
				if i == 0:
					random.shuffle(myList)
					random.shuffle(myList2)
					random.shuffle(myList3)

				# leaves sorted list sorted
				elif i == 2:
					pass

				# reverses a list
				elif i == 3:
					myList[::-1]
					myList2[::-1]
					myList3[::-1]

				# makes list into almost sorted
				else:
					almostSorted(myList)
					almostSorted(myList2)
					almostSorted(myList3)

				# add time 
				time += functionTimer(sortMethods[i], myList)
				time2 += functionTimer(sortMethods[i], myList2)
				time3 += functionTimer(sortMethods[i], myList3)

			# calculate avg time
			avgTime = time / 5
			avgTime2 = time2 / 5 
			avgTime3 = time3 / 5

			# format avg time
			f_avgTime = "{:.6f}".format(avgTime)
			f_avgTime2 = "{:.6f}".format(avgTime2)
			f_avgTime3 = "{:.6f}".format(avgTime3)
			# print avg time
			print("{:>12} {:>11} {:>11}".format(f_avgTime, f_avgTime2, f_avgTime3))

		print()
		print()
main()