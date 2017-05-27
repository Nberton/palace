class Card(object):
	"""Card object which a deck is made of"""
	def __init__(self,suitName,val):
		if val < 2:
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
