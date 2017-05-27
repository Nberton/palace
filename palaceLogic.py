from card import Card

# non-member function but necessary to game logic
def card_priority(x,y):
	# 2s reset and can be played whenever
	# 10s dump so are equally good
	# otherwise value order
	if x.value == 2 or x.value == 10:
		if y.value ==2 or y.value == 10:
			return 0
		else: 
			return 1
	if y.value==2 or y.value==10:
		return -1
	if x.value == y.value:
		return 0
	if x.value > y.value:
		return 1
	return -1
		

def test_card_priority_twos():
	card1 = Card('Clubs',2)
	card2 = Card('Hearts',2)
	assert(card_priority(card1,card2) == 0)