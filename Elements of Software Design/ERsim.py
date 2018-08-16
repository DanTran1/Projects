#  File: ERsim.py
#  Description: simulating the environment of a busy Emergency Room (ER) for a hospital
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 10/20/17
#  Date Last Modified: 10/20/17

# create class Queue
class Queue:

    def __init__(self):
        self.items = []

    # add item to queue
    def enqueue(self,item):
        self.items.append(item)

    # remove item from queue
    def dequeue(self):
        return self.items.pop(0)

    # check if queue is empty
    def isEmpty(self):
        return self.items == []

    # return length of queue
    def size(self):
        return len(self.items)

    # return first item of queue
    def peek(self):
        return self.items[0]

    # prints queue backward
    def __str__(self):
    	return str(self.items[::-1])

# create queues for 3 conditions
FAIR = Queue()
SERIOUS = Queue()
CRITICAL = Queue()

# print all queues
def print_queues():

	print("\tQueues are:")
	print("\tFair:    ", FAIR)
	print("\tSerious: ", SERIOUS)
	print("\tCritical:", CRITICAL)
	print()
	print()

# add patient to queues
def add(info):

	condition = info[1]

	patient_name = info[2]

	print("Command: Add patient", patient_name, "to ", end = "")

	# add patient to queue, based on their condition
	if condition == "Critical":

		CRITICAL.enqueue(patient_name)
		print("Critical queue\n")

	elif condition == "Serious":

		SERIOUS.enqueue(patient_name)
		print("Serious queue\n")

	else:

		FAIR.enqueue(patient_name)
		print("Fair queue\n")

	# print queue
	print_queues()

# treat patients and take them off queue
# or print there is no patients in queue
def treat(queue, condition):

	if queue.isEmpty():

		print("\tNo patients in queue\n")

	else:

		print("\tTreating", queue.dequeue(), "from", condition, "queue")

	print_queues()

# handle 3 different types of treating commands
# do different things based on treat next, all, or a specific condition
def sort_treat(info):

	print("Command: Treat ", end = "")

	command = info[1]

	# command is treat next
	if command == "next":

		print("next patient")
		print()

		# treat patients in order of critical, serious, then fair
		if CRITICAL.isEmpty() == False:

			treat(CRITICAL, "Critical")

		elif SERIOUS.isEmpty() == False:

			treat(SERIOUS, "Serious")

		elif FAIR.isEmpty() == False:

			treat(FAIR, "Fair")

		else:

			print("\tNo patients in queues\n")

	# treat a specific condition
	elif command in ["Fair", "Serious", "Critical"]:

		print("next patient on ", end ="")

		# determine which queue condition is called for
		if command == "Fair":

			print("Fair queue")
			print()

			treat(FAIR, "Fair")

		elif command == "Serious":

			print("Serious queue")
			print()

			treat(SERIOUS, "Serious")

		else:

			print("Critical queue")
			print()

			treat(CRITICAL, "Critical")	


	# treat all command
	else:

		print("all patients")
		print()
		
		# treat patients in the same order as treat next
		# until all queue is empty
		while True:

			if CRITICAL.isEmpty() == False:

				treat(CRITICAL, "Critical")

			elif SERIOUS.isEmpty() == False:

				treat(SERIOUS, "Serious")

			elif FAIR.isEmpty() == False:

				treat(FAIR, "Fair")

			else:

				print("\tNo patients in queues\n")
				break

# determine the command add, treat, or exit
def sort_queue(info):

	command = info[0]

	if command == "add":

		add(info)

	elif command == "treat":

		sort_treat(info)

	else:

		print("Command: Exit")
		exit()

def main():

	# open file in read mode
	file = open("ERsim.txt","r")

	# read each line in the file
	for line in file:

		# strip unnecessary chararcters
		# and parse each command line
		line = line.rstrip("\n")
		line = line.split()
		sort_queue(line)

	# close the file once it is read
	file.close()


main()

