#Nathan Berton
#Card Game
#Southwest Flight LAS to PHL 6/8/2016
#IND Airport 5/26/2017
from player import Player
from deck import Deck
from card import Card


def main():
	print "Welcome to PALACE"
	numPlayers = input("Please Enter Number of AI Players: ") + 1
	numDecks = input("Please enter the number of decks to be used:")
	deck = Deck(1)
	# Oh look list comprehensions!
	players = [Player() for n in range(numPlayers)]
	
	

if __name__ == '__main__':
	main()