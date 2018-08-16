#  File: htmlChecker.py
#  Description: checks html document
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 10/12/17
#  Date Last Modified: 10/13/17

VALIDTAGS = []
EXCEPTIONS = ["br","meta","hr"]

# create stack class
class Stack(object):

    def __init__(self):
    	self.items = [ ]

    def isEmpty (self):
       	return self.items == [ ]

    def push (self, item):
       	self.items.append(item)

    def pop (self):
       	return self.items.pop()

    def peek (self):
       	return self.items[len(self.items)-1]

    def size (self):
       	return len(self.items)

    def __str__ (self):
       	return str(self.items)

# get tag out of list of characters from file
def get_tag(str_list):

	while len(str_list) != 0:
		# if open tag is found break
		# remove the open tag
		if str_list[0] == "<":

			del str_list[0]
			break
		# remove all strings before the open tag
		else:

			del str_list[0]

	tag = ""
	
	while len(str_list) != 0:
		# if closing tag is found delete it
		# get out of the loop
		if str_list[0] == ">" or str_list[0] == " ":

			del str_list[0]
			break
		# add character to the tag string 
		# then delete the character from the list
		else:
			tag += str_list[0]
			del str_list[0]		
	# return the tag
	if tag == "":

		return None

	else:

		return tag


def main():
	# open file
	f = open("htmlfile.txt","r")
	# read the fil
	f = f.read()
	f_string = []
	# each character into a list
	for char in f:

		f_string.append(char)

	tag_list = []

	not_done = True

	while not_done:
		# get the tag 
		tag = get_tag(f_string)
		
		if tag == None:

			not_done = False
			break
		# add to list
		tag_list.append(tag)

	print(tag_list)
	# create a stack 
	start_tags = Stack()

	try:
		# check list of tags
		for t in tag_list:
			# if tag is an end tag
			# check if it matches the top of the start tag stack
			if t.startswith("/"):

				end_tag = t[1:]

				if end_tag == start_tags.peek():
					
					start_tags.pop()
					print("Tag", t, "matches top of stack: stack is now", start_tags)

				else:

					raise ERROR
					break
			# checks if tags don't need closing tags
			elif t in EXCEPTIONS:

				print("Tag", t, "does not need a match: stack is still", start_tags)
			
			# if tag is an open tag then add it to the stack
			else:
				# add new tags to VALIDTAG list
				if t not in VALIDTAGS:

					VALIDTAGS.append(t)
					print("New tag", t, "found and added to list of valid tags")

				start_tags.push(t)
				print("Tag", t, "pushed: stack is now", start_tags)
		# checks if stack is empty
		if start_tags.isEmpty():

			print("Processing complete. No mismatches found.")

		else:

			print("Processing complete. Unmatched tags remain on stack:", start_tags)
	# error if closing tag does not match top of stack
	except ERROR:

		print("Error: tag is", t, "but top of the stack is", start_tags.peek())


	print("Valid tags: ", VALIDTAGS)
	print("Exceptions: ", EXCEPTIONS)

main()
