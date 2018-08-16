#  File: War.py
#  Description: Simulation of War Game
#  Student's Name: Tam Dan Tran
#  Student's UT EID: tvt287	
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 10/05/17
#  Date Last Modified: 10/06/17

import random

# create global variables for card numbers and suits
CARD_SUITS = ("C","D","H","S")
CARD_RANKS = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")

# create class Card
class Card: 
	# each card has a suit and rank
	def __init__(self, rank, suit):

		self.rank = rank
		self.suit = suit
		
	# return string that displays card rank and suit
	def __str__(self):

		card_string = str(self.rank) + self.suit

		return card_string

# create class Deak
class Deck:

	# create card list that has all 52 cards 
	def __init__(self):

		self.card_list = []

		for i in CARD_SUITS:
			for j in CARD_RANKS:
				card = Card(j,i)
				self.card_list.append(card)

	# shuffle the card
	def shuffle(self):

		random.shuffle(self.card_list)

	# deal cards into player's hands
	def deal_one(self, player):

		dealt_card = self.card_list.pop(0)

		player.hand.append(dealt_card)
		player.hand_total += 1

	# print deck neatly and move to next line for every 13 card printed
	def __str__(self):

		deck_string = ""

		for i in range(len(self.card_list)):

			card_13 = [12,25,38,51]

			card = self.card_list[i] 

			deck_string += "{:>4}".format(str(card))

			if i in card_13:

				deck_string += "\n"

		return deck_string

# create class Player
class Player:

	# each player has an amount of cards in hand
	def __init__(self):

		self.hand = []
		self.hand_total = 0

	def hand_not_empty(self):

		return self.hand_total != 0

	# print player's deck neatly and move to next line
	# for every 13 card printed
	def __str__(self):
		
		hand_string = ""

		for i in range(len(self.hand)):

			card_13 = [12,25,38,51]

			hand_string += "{:>4}".format(str(self.hand[i])) 

			if i in card_13:

				hand_string += "\n"


		return hand_string

# create a function to simulate the game
def play_game(card_deck,player1,player2):

	# start counting rounds
	game_round = 1
	war_begin = True

	# print initial decks
	print("Initial hands:")
	print("Player 1:")
	print(player1)
	print("Player 2:")
	print(player2)

	# play game while both players still have cards
	while player1.hand_not_empty() and player2.hand_not_empty():

		# create pile for each players discarded cards
		played_cards_p1 = []
		played_cards_p2 = []

		print("ROUND " + str(game_round) + ":")
		# each player puts out a card 
		card_player1 = player1.hand.pop(0)
		played_cards_p1.append(card_player1)
		player1.hand_total -= 1
		print("Player 1 plays:", card_player1)

		card_player2 = player2.hand.pop(0)
		played_cards_p2.append(card_player2)
		player2.hand_total -= 1
		print("Player 2 plays:", card_player2)
		print()

		# if cards are equal in ranks, war begins
		if CARD_RANKS.index(card_player1.rank) == CARD_RANKS.index(card_player2.rank):

			if war_begin:
				print("War Starts:", end =" ")

			else: 
				print("War Continues:", end =" ")

			print(card_player1, "=", card_player2)

			war_begin = False
			# each player puts 3 cards face down
			for i in range(3):

				war_card_p1 = player1.hand.pop(0)
				print("Player 1 puts", war_card_p1, "face down")
				player1.hand_total -= 1
				played_cards_p1.append(war_card_p1)

				war_card_p2 = player2.hand.pop(0)
				print("Player 2 puts", war_card_p2, "face down")
				player2.hand_total -= 1
				played_cards_p2.append(war_card_p2)

			# each player puts a card face up
			card_player1 = player1.hand.pop(0)
			played_cards_p1.append(card_player1)
			player1.hand_total -= 1
			print("Player 1 puts", card_player1, "face up")

			card_player2 = player2.hand.pop(0)
			played_cards_p2.append(card_player2)
			player2.hand_total -= 1
			print("Player 2 puts", card_player2, "face up")

		# if player 1 has higher ranked card, then they win the round
		if CARD_RANKS.index(card_player1.rank) > CARD_RANKS.index(card_player2.rank):

			print("Player 1 wins round", game_round,":", card_player1, ">", card_player2)
			# add both piles of cards into the player 1 hand
			# add to bottom of the stack
			player1.hand.extend(played_cards_p1)
			player1.hand.extend(played_cards_p2)
			player1.hand_total += len(played_cards_p1) + len(played_cards_p2)
			# count rounds
			game_round += 1

			war_begin = True
		# if player 2 has higher ranked card, then they win the round
		elif CARD_RANKS.index(card_player1.rank) < CARD_RANKS.index(card_player2.rank):

			print("Player 2 wins round", game_round,":", card_player2, ">", card_player1)
			# add both piles of cards into the player 2 had
			# add to bottom of the stack
			player2.hand.extend(played_cards_p1)
			player2.hand.extend(played_cards_p2)
			player2.hand_total += len(played_cards_p1) + len(played_cards_p2)
			# count rounds
			game_round += 1

			war_begin = True
		# print each players hand total and hand
		print()
		print("Player 1 now has", player1.hand_total, "card(s) in hand:")
		print(player1)
		print("Player 2 now has", player2.hand_total, "card(s) in hand:")
		print(player2)
		print()



def main():

	# create a deck of 52 cards called "cardDeck"
    card_deck = Deck() 
    # print the deck so we can see that you built it correctly              
    print("Initial deck:")
    print(card_deck)					
    
    # leave this in for grading purposes
    random.seed(15)  
    # shuffle the deck              
    card_deck.shuffle()
    # print the deck so we can see that your shuffle worked              
    print("Shuffled deck:")
    print(card_deck)                 
    
    # create a player
    player1 = Player()      
    # create another player        
    player2 = Player() 

    # deal 26 cards to each player, one at              
	# a time, alternating between players
    for i in range(26):             
       card_deck.deal_one(player1)   
       card_deck.deal_one(player2)

    play_game(card_deck,player1,player2)

    if player1.hand_not_empty():
    	print("\n\nGame over.  Player 1 wins!")

    else:
    	print("\n\nGame over.  Player 2 wins!")
    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    # printing a player object should print that player's hand
    print (player1)                 
    print ("\nPlayer 2:")
    # one of these players will have all of the cards, the other none
    print (player2)                 

main()











