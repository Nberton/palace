

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
		print "UNDER CONSTRUCTION YA GOOF"
		# put all the cards into 1 list 
		# sort them using a custom sort function
		# take the best three and put them on top (this may not be best play)
