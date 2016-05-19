
# Show the card layout
# Create a dictionary to store the card coordinate and its associated images
 # The images represent when the card is revealed
# Set the counter to 0 for the turn
# Prompt the user to pick a card
 # Reveal the card
# Prompt the user to pick a card
 # Reveal the card
 # If the RC 1 (revealed card) == RC 2:
  # match! print text
  # delete the matched cards from the dictionary for the end game condition
  # else:
  # not a match! print text and continue until all cards are matched
 # Increment the counter for the turns
 # When the dictionary is empty, print how many turns it took to complete the game

print "There are 4 cards. Pick 2 cards to match them."

print "+------+------+"
print "| card | card |"
print "+------+------+"
print "|  1   |  2   |"
print "+------+------+"
print "|  3   |  4   |"
print "+------+------+"
print

# The value is the card coordinate and the key is the hidden image
cards = {"1": "O", "2": "X", "3": "X", "4": "O"}

count = 0

while cards !={}:
	card_pick1 = raw_input("Pick a card: ")
	picked_card1 = cards[card_pick1]
	print "Your card is {}".format (picked_card1)
	print
	
	card_pick2 = raw_input("Pick a card: ")
	picked_card2 = cards[card_pick2]
	print "Your card is {}".format (picked_card2)
	print
py
	if picked_card1 == picked_card2:
		del cards[card_pick1], cards[card_pick2]
		print "The cards match!"
		print
	else:
		print "The cards don't match!"
		print

	count +=1

print "It took you {} turns".format (count)