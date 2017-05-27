import random
from card import Card

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
					self.activeDeck.append((Card(s,c)))
		#cards all created
		print ("Deck Created of size " + str(len(self.activeDeck)) + " should be " + str(numDecks*13*4))
		#no shuffle as we pull cards randomly

	def get_cards_remaining(self):
		return len(self.activeDeck)

	def draw(self):
		if len(self.activeDeck)  == 0:
			return False
		index = random.randint(0,len(self.activeDeck)-1)
		card =	self.activeDeck.pop(index)
		return card
