#  File: Friends.py
#  Description: simulate facebook
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 11/09/17
#  Date Last Modified: 11/10/17

# create node object
class Node(object):
	def __init__(self,initdata):
		self.data = initdata
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newData):
		self.data = newData
	def setNext(self,newNext):
		self.next = newNext
# create unorderedlist object
class UnorderedList(object):
	def __init__(self):
		sentinel = Node(None)
		self.head = sentinel
	def isEmpty(self):
		return self.head.getNext() == None
	def add(self,item):
		# add a new Node to the beginning of existing list
		temp = Node(item)
		temp.setNext(self.head.getNext())
		self.head.setNext(temp)
	def length(self):
		current = self.head.getNext()
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count
	# search in unordered list
	def search(self,item):
		current = self.head.getNext()
		found = False
		while current != None and not found:
			if current.getData().name == item:
				found = True
			else:
				current = current.getNext()
		return found
	def remove(self,item):
		current = self.head.getNext()
		previous = self.head
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		previous.setNext(current.getNext())
	# return element from unordered list (object)
	def getElement(self,item):
		current = self.head.getNext()
		found = False
		while current != None and not found:
			if current.getData().name == item:
				found = True
			else:
				current = current.getNext()
		return current.getData()
	# returns a string of all elements inside list
	def __str__(self):
		string = " "
		current = self.head.getNext()
		while current != None:
			string += current.getData().name + " "
			current = current.getNext()
		return string

# create user object
class User(object):
	def __init__(self,name):
		self.name = name
		self.friends = UnorderedList()
	# add friend method
	def addFriend(self, n2):
		self.friends.add(n2)
	# print a list of friends
	def listFriend(self):
		friends = "[" + str(self.friends) + "]"
		return friends
	# delete friend method
	def unFriend(self, n2):
		self.friends.remove(n2)

# create a global variable of unordered list
ALL_USERS = UnorderedList()

# create exceptions
# account already exists exception
class accountExistError(Exception):
	def __init__(self,account_name):
		self.account_name = account_name
	def __str__(self):
		return("A person with name " + self.account_name + " already exists.")
# account does not exists exception
class accountNotExistError(Exception):
	def __init__(self, account_name):
		self.account_name = account_name
	def __str__(self):
		return("A person with name " + self.account_name + " does not currently exist.")
# refering to same account exception
class sameAccountError(Exception):
	def __init__(self, action):
		self.action = action
	def __str__(self):
		if self.action == "Friend":
			return("A person cannot friend him/herself.")
		else:
			return("A person cannot unfriend him/herself.")
# already friends exception
class friendExistError(Exception):
	def __init__(self, account_name1, account_name2):
		self.account_name1 = account_name1
		self.account_name2 = account_name2
	def __str__(self):
		return(self.account_name1 + " and " + self.account_name2 + " are already friends.")
# not friends exception, so can't unfriend
class unfriendError(Exception):
	def __init__(self, account_name1, account_name2):
		self.account_name1 = account_name1
		self.account_name2 = account_name2
	def __str__(self):
		return(self.account_name1 + " and " + self.account_name2 + " aren't friends, so you can't unfriend them.")

def main():
	# open file
	f = open("FriendData.txt","r")
	# read each line
	for line in f:
		line = line.strip()
		print("-->",line)
		print("    ", end ="")
		line = line.split()

		command = line[0]

		# exits program
		if len(line) == 1:
			print("Exiting...")
			exit()	

		else:	
			name1 = line[1]
			if len(line) == 2:
				# execute creation of account command
				if command == "Person":
					try:
						# raise already user exception
						if ALL_USERS.search(name1):
							raise accountExistError(name1)
						# create new user and add to global unordered list
						else:
							newUser = User(name1)
							print(newUser.name, "now has an account.")
							ALL_USERS.add(newUser)
					except accountExistError as error:
						print(error)
				# execute printing of friend's list command
				elif command == "List":
					try:
						# if user exist, continue
						if ALL_USERS.search(name1):	
							user = ALL_USERS.getElement(name1)
							# print user list of friends
							if not user.friends.isEmpty():
								print(user.listFriend())
							else:
								print(user.name, "has no friends.")
						# if user does not exist, raise exception
						else:
							raise accountNotExistError(name1)
					except accountNotExistError as error:
						print(error)

			else:
				name2 = line[2]

				try:
					# checks if same person
					if name1 == name2:
						raise sameAccountError(command)
					# checks if not a user
					elif not ALL_USERS.search(name1):
						raise accountNotExistError(name1)
					# checks if not a user
					elif not ALL_USERS.search(name2):
						raise accountNotExistError(name2)
					# execute command adding friends
					if command == "Friend":

						# checks if already friends
						if ALL_USERS.getElement(name1).friends.search(name2):
							raise friendExistError(name1,name2)
						# add friends
						else:
							user1 = ALL_USERS.getElement(name1)
							user2 = ALL_USERS.getElement(name2)
							user1.addFriend(user2)
							user2.addFriend(user1)
							print(user1.name, "and", user2.name, "are now friends.")
					# execute command for unfriending
					elif command == "Unfriend":
						# unfriend people
						if ALL_USERS.getElement(name1).friends.search(name2):
							user1 = ALL_USERS.getElement(name1)
							user2 = ALL_USERS.getElement(name2)
							user1.unFriend(user2)
							user2.unFriend(user1)
							print(user1.name, "and", user2.name, "are no longer friends.")
						# if not friends, rause unfriend exception
						else:
							raise unfriendError(name1,name2)
					# execute command for query 
					else:
						if ALL_USERS.getElement(name1).friends.search(name2):
							print(name1, "and", name2, "are friends.")
						else:
							print(name1, "and", name2, "are not friends.")
				# catches exception
				except accountNotExistError as error:
					print(error)
				except sameAccountError as error:
					print(error)
				except friendExistError as error:
					print(error)
				except unfriendError as error:
					print(error)

		print()


main()






