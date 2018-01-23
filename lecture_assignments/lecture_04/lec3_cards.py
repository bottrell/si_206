import random
import unittest

######### DO NOT CHANGE PROVIDED CODE #########

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
        return "{} of {}".format(self.rank_num,self.suit)

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
        return self.cards.pop(i) # this card is no longer in the deck -- taken off

    def shuffle(self):
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] 
        # forming an empty list
        for c in self.cards: 
        # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) 
            # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs:
         # if the string representing this card is not in the list already
            self.cards.append(card) 
            # append it to the list

    def sort_cards(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.pop_card(i))
        return hand_cards


# A silly function, but it does kind of work to play a game.
# Because it's written in a silly way, there are a bunch of edge cases of sorts.
def play_war_game(testing=True):
    # Call this with testing = True and it won't print out all the game mechanics, which makes it easier to see tests.
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



########### DO NOT CHANGE CODE ABOVE THIS LINE ###############

##### IMPLEMENT UNIT TESTS HERE ####

class TestCard(unittest.TestCase):
    def test_init(self):
        c1 = Card(0,1)
        c2 = Card(2,11)

        self.assertEqual(c1.suit, "Diamonds")
        self.assertEqual(c1.rank_num, 1)
        self.assertEqual(c2.suit, "Hearts")
        self.assertEqual(c2.rank_num, 11)
#write tests that:
#   test the deck is the right size
#   test that pop_card() works as specified
#   test that replace_card() works as specified
#   test that shuffle() and sort_cards() works as specified
class TestDeck(unittest.TestCase):
    
    def test_size(self):
        D1 = Deck()
        self.assertEqual(len(D1.cards), 52)

    def test_pop(self):
        D1 = Deck()
        card = D1.pop_card()
        self.assertEqual(card.__str__(), "13 of Spades")
        card2 = D1.pop_card()
        self.assertEqual(card2.__str__(), "12 of Spades")
   
    def test_replace(self):
        D1 = Deck()
        card = Card(0,1)
        card2 = Card(3,13)
        for x in range(52):
            D1.pop_card()

        self.assertEqual(len(D1.cards), 0)
        D1.replace_card(card)
        self.assertTrue(card in D1.cards)
        self.assertEqual(len(D1.cards),1)
        D1.replace_card(card2)
        self.assertTrue(card2 in D1.cards)

    def test_shuffle(self):
        D1 = Deck()
        self.assertTrue(len(D1.cards),52)
        card = D1.cards[13]
        D1.shuffle()
        self.assertTrue(len(D1.cards),52)
        card_compare = D1.cards[13]
        self.assertNotEqual(card, card_compare)

    def test_sort(self):
        D1 = Deck()
        D1.shuffle()
        deck_1_cards = D1.cards
        D2 = Deck()
        deck_2_cards = D2.cards
        self.assertNotEqual(deck_1_cards, deck_2_cards)


unittest.main()
