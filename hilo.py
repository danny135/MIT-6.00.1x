# Paste your code into this box
done = False
print "Please think of a number between 0 and 100!"
lowest = 0
highest = 100
guess = 50
while not done:
	print "Is your secret number " + str(guess) + "?"
	input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if input == "c":
		print "Game over. Your secret number was:", guess
		break
	elif input == "h":
		highest = guess
		guess = (highest + lowest) / 2
	elif input == "l":
		lowest = guess
		guess = (highest + lowest) / 2
	else:
		print "Sorry, I did not understand your input."
		
raw_input()