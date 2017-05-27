from card import Card
	
# probably useless to you on a plane but here is the documentation
# https://docs.python.org/2/library/functions.html#cmp
# its the cmp function we are basing this on
# cmp(x,y) 
# important part is -1 means x < y , 0 means x == y , 1 means x > y

# Function for the AI to determine card priority in Palace
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
		

# UNIT TESTS
def test_card_priority_twos():
	card1 = Card('Clubs',2)
	card2 = Card('Hearts',2)
	assert(card_priority(card1,card2) == 0)

def test_card_priority_tens():
	card1 = Card('Clubs',10)
	card2 = Card('Hearts',10)
	assert(card_priority(card1,card2) == 0)

def test_card_priority_ten_two():
	card1 = Card('Clubs',2)
	card2 = Card('Hearts',10)
	assert(card_priority(card1,card2) == 0)

def test_card_priority_ace_5():
	card1 = Card('Clubs',14)
	card2 = Card('Hearts',5)
	assert(card_priority(card1,card2) == 1)

def test_card_priority_5_ace():
	card1 = Card('Clubs',5)
	card2 = Card('Hearts',14)
	assert(card_priority(card1,card2) == -1)

def test_card_priority_5_queen():
	card1 = Card('Clubs',5)
	card2 = Card('Hearts',12)
	assert(card_priority(card1,card2) == -1)