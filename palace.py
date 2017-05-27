#Nathan Berton
#Card Game
#Southwest Flight LAS to PHL 6/8/2016
#IND Airport 5/26/2017
from player import Player
from deck import Deck
from card import Card

def new_game(players,deck):
	for i in xrange(len(players)*3): #deal each player 3 under cards 
		players[(i%len(players))].under.append(deck.draw())
	#seperate for loops because of sequence of deals
	for j in xrange(len(players*3)): # 3 top cards (handle replacement after hand deal)
		players[(j%len(players))].top.append(deck.draw())
	for k in xrange(len(players*6)):
		players[(k%len(players))].hand.append(deck.draw())

def main():
	print "Welcome to PALACE"
	numPlayers = input("Please Enter Number of AI Players: ") + 1
	numDecks = input("Please enter the number of decks to be used:")
	deck = Deck(numDecks)
	# Oh look list comprehensions!
	players = [Player() for n in range(numPlayers)]
	print str(len(players)) + " Players in the game"\

if __name__ == '__main__':
	main()


# OH LOOK SOME TESTS BATMAN!
# written for py.test so pip install pytest
# and yes I am writing unit tests that are entirely procastinatory in nature
def test_new_game():
	deck = Deck(1)
	players = [Player() for i in range(3)]
	new_game(players,deck)
	valid = True
	assert(deck.get_cards_remaining() == (52 - (12*3)))
	for player in players:
		assert(len(player.under) == 3)
		assert(len(player.top) == 3)
		assert(len(player.hand) == 6)
	