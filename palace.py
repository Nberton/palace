#Nathan Berton
#Card Game
#Southwest Flight LAS to PHL 6/8/2016
import random

class Card(object):
	"""Card object which a deck is made of"""
	def __init__(self,suitName,val):
		if value < 2:
			print "Invalid Card created and this is a hastily written program so...."
			print "Exiting!"
			exit(1)
		super(Card, self).__init__()
		self.suit = suitName
		self.value = val

	def str(self):
		#figure out value
		valStr = ""
		if self.value <10:
			valStr = str(self.value)
		elif self.value == 10:
			valStr = "Jack"
		elif self.value == 11:
			valStr = "Queen"
		elif self.value == 12:
			valStr = 'King'
		elif self.Value == 13:
			valStr = 'Ace'
		#suit is already a string so return nice format
		return valStr + " of " + self.suit

	def shortP(self):
		if self.value <10:
			valStr = str(self.value)
		elif self.value == 11:
			valStr = "Jack"
		elif self.value == 12:
			valStr = "Queen"
		elif self.value == 13:
			valStr = 'King'
		elif self.Value == 14:
			valStr = 'Ace'
		#suit is already a string so return nice format
		return valStr + ":" + self.suit[0]		


class Deck(object):
	"""Holds the Cards for the Game: Deals Cards without replacement"""
	def __init__(self,numDecks):
		super(Deck, self).__init__()
		self.activeDeck = list()
		suits = ["Diamonds","Hearts","Clubs","Spades"]
		for i in range(0,numDecks):
			#4 suits
			for s in suits:	
				for c in range(2,15):  #13 cards per suit 
					self.activeDeck.push_back(Card(s,c))
		#cards all created
		print "Deck Created of size " + str(len(self.activeDeck)) + " should be " + str(numDecks*13*4)
		#no shuffle as we pull cards randomly

	def draw(self):
		if len(self.activeDeck)  == 0:
			return False
		index = random.randint(0,len(self.activeDeck)-1)
		card =	self.activeDeck.pop(index)
		return card

class Player(object):
	"""Player Class Base structure"""
	def __init__(self, sd):
		super(Player, self).__init__()
		self.hand = list()
		self.deck = sd
		self.under = list() #represents face down
		self.top = list() #represents face up cards


def main():
	print "Welcome to PALACE"
	numPlayers = input("Please Enter Number of AI Players: ")
	numDecks = input("Please enter the number of decks to be used:")
	deck = Deck(1)
	players = list()
	for i in range(0,numPlayers+1):
		players.push

if __name__ == '__main__':
	main()