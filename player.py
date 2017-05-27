import palaceLogic
from card import Card

class Player(object):
	"""Player Class Base structure"""
	def __init__(self):
		super(Player, self).__init__()
		self.hand = list()
        # Don't know why I thought I needed this
		# self.deck = sd
		self.under = list() #represents face down
		self.top = list() #represents face up cards
	
	def adjust_top(self):
		# put all the cards into 1 list 
		activeCards = self.hand + self.top		# sort them using a custom sort function
		# sort them using a custom sort function
		activeCards.sort(cmp=palaceLogic.card_priority,reverse=True)
		for card in activeCards:
			print card 
		# take the best three and put them on top (this may not be best play)
		self.top = activeCards[:3]
		# Put the rest back in the hand
		self.hand = activeCards[3:]

	def print_hand(self):
		print "The Hand is: "
		for card in self.hand:
			print str(card)

	def print_top(self):
		print "Face up Cards are: "
		for card in self.top:
			print str(card)


def test_adjust_top():
	player = Player()
	player.top = [Card('Hearts',2),Card('Hearts',5),Card('Hearts',8)]
	player.hand = [Card('Clubs',2),Card('Clubs', 10),Card('Clubs',7),Card('Clubs',9),Card('Clubs',14),Card('Clubs',5)]
	player.adjust_top()
	player.print_hand()
	player.print_top()
	# assert(player.top() == [Card(Hearts,2)])