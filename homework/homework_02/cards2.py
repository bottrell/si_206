import random
import unittest

# SI 206 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Wednesday 9am

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########
class Hand(object):
	cards = []
	# create the Hand with an initial set of cards
	# param: a list of cards
	def __init__(self, init_cards = []):
		self.cards = init_cards

	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
	def add_card(self, card):
		if card in self.cards:
			return
		else:
			self.cards.append(card)

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand
	def remove_card(self, card):
		if card not in self.cards:
			return None

		else:
			self.cards.remove(card)

	#draw a card from a deck and add it to the hand
	#side effect: the deck will be depleted by one card
	#param: the deck from which to draw
	#returns: nothing
	def draw(self, deck):
		new_card = deck.pop_card()
		self.cards.append(new_card)


class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=True):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p2 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code in this section...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########

'''


(and 16)  Write at least 2 additional tests. Make sure to include a descriptive message in these two so we can easily see what you are testing!
'''






##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):


	# this is a "test"
	def test_create(self):
		card1 = Card()
		self.assertEqual(card1.suit, "Diamonds")
		self.assertEqual(card1.rank, 2)


	'''
	xx Test that if you create a card with rank 12, its rank will be "Queen"
	xx Test that if you create a card with rank 1, its rank will be "Ace" 
	xx Test that if you create a card instance with rank 3, its rank will be 3
	'''
	def test_rank(self):
		card2 = Card(0, 12)
		self.assertEqual(card2.rank, 'Queen')

		card3 = Card(0, 1)
		self.assertEqual(card3.rank, 'Ace')

		card4 = Card(0, 3)
		self.assertEqual(card4.rank, 3)
	
	'''
	xx Test that if you create a card instance with suit 1, it will be suit "Clubs"
	xx Test that if you create a card instance with suit 2, it will be suit "Hearts"
	'''
	def test_suit(self):
		card5 = Card(1 ,1)
		self.assertEqual(card5.suit, 'Clubs')

		card6 = Card(2,1)
		self.assertEqual(card6.suit, 'Hearts')
	'''
	xx Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	'''
	def test_suit_names_in_instance(self):
		card7 = Card()
		self.assertEqual(card7.suit_names, ["Diamonds","Clubs","Hearts","Spades"])

	'''
	xx Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
	xx Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades" 
	'''
	def test_str(self):
		card8 = Card(2,7)
		self.assertEqual(card8.__str__() ,"7 of Hearts")

		card9 = Card(3, 13)
		self.assertEqual(card9.__str__(), "King of Spades" )

	#Test that if you create a deck instance, it will have 52 cards in its cards instance variable
	def test_deck_size(self):
		deck1 = Deck()
		self.assertEqual(len(deck1.cards), 52)

	'''
	xxTest that if you invoke the pop_card method on a deck, it will return a card instance.
	xxTest that if you invoke the pop_card method on a deck, the deck has one fewer cards in it afterwards.
	'''
	def test_deck_pop_card(self):
		deck1 = Deck()

		deck_card = deck1.pop_card()
		self.assertIsInstance(deck_card, Card)

		self.assertEqual(len(deck1.cards), 51)

	'''
	xxTest that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use pop_card function first to remove a card from the deck and then replace the same card back in)
	xxTest that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)
	'''
	def test_replace_card(self):
		deck1 = Deck()

		deck_card = deck1.pop_card()
		self.assertIsInstance(deck_card, Card)

		self.assertEqual(len(deck1.cards), 51)

		bad_replacement = Card(0, 3)
		deck1.replace_card(bad_replacement)
		self.assertEqual(len(deck1.cards), 51)

		deck1.replace_card(deck_card)
		self.assertEqual(len(deck1.cards), 52)

		deck1.replace_card(deck_card)
		self.assertEqual(len(deck1.cards), 52)

	#Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple test methods!)
	def test_play_war_game(self):
		tup = play_war_game()
		self.assertIsInstance(tup[0], str)
		self.assertEqual(len(tup), 3)
		self.assertIsInstance(tup, tuple)


	#Write at least 2 additional tests. Make sure to include a descriptive message in these two so we can easily see what you are testing!
	#test that shuffling the deck will not add or delete cards
	#checks that the 14th card in the deck is different after shuffling
	#there is a 1 in 52 possibltiy that the test will fail because the random element will put the
	#card back at it's initial location
	def test_shuffle(self):
		D1 = Deck()
		self.assertTrue(len(D1.cards),52)
		card = D1.cards[13]
		D1.shuffle()
		self.assertTrue(len(D1.cards),52)
		card_compare = D1.cards[13]
		self.assertNotEqual(card, card_compare)

	#shuffle the deck, then sort the deck, and check and make sure that they're not the same
	def test_sort(self):
		D1 = Deck()
		D1.shuffle()
		deck_1_cards = D1.cards
		D2 = Deck()
		deck_2_cards = D2.cards
		self.assertNotEqual(deck_1_cards, deck_2_cards)
		

class TestHand(unittest.TestCase):
	'''
	Test that a hand is initialized properly.
	Test that add_card( ) and remove_card( ) behave as specified (you can write one test for this, called testAddAndRemove.
	Test that draw( ) works as specified. Be sure to test side effects as well.
	'''

	def test_init(self):
		card1 = Card()
		card2 = Card(0,2)
		card3 = Card(0,3)
		cards = [card1, card2, card3]
		my_hand = Hand(cards)
		self.assertEqual(my_hand.cards, cards)

	def test_add_and_remove(self):
		my_hand = Hand()
		card1 = Card()

		my_hand.add_card(card1)
		self.assertEqual(len(my_hand.cards), 1)
		self.assertEqual(my_hand.cards[0].__str__(), "2 of Diamonds")
		my_hand.remove_card(card1)

		self.assertEqual(len(my_hand.cards), 0)

	'''

	#draw a card from a deck and add it to the hand
	#side effect: the deck will be depleted by one card
	#param: the deck from which to draw
	#returns: nothing
	def draw(self, deck):
		new_card = deck.pop_card()
		self.cards.append(new_card)

    '''

	def test_draw(self):
		deck = Deck()
		my_hand = Hand()
		my_card = deck.cards[-1]
		my_card2 = deck.cards[-2]
		
		my_hand.draw(deck)
		self.assertEqual(my_hand.cards[0], my_card)

		my_hand.draw(deck)
		self.assertEqual(my_hand.cards[1], my_card2)



## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.