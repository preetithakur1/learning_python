import random

def hang(guesses,wd):
	if(guesses == 0):
		print("_______________")
		print("|      |")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|______________")
	elif(guesses == 1):
		print("_______________")
		print("|      |")
		print("|      O")
		print("|")
		print("|")
		print("|")
		print("|______________")
	elif(guesses == 2):
		print("_______________")
		print("|      |")
		print("|      O")
		print("|      |")
		print("|      |")
		print("|")
		print("|______________")
	elif(guesses == 3):
		print("_______________")
		print("|      |")
		print("|      O")
		print("|     \|")
		print("|      |")
		print("|")
		print("|______________")
	elif(guesses == 4):
		print("_______________")
		print("|      |")
		print("|      O")
		print("|     \|/")
		print("|      |")
		print("| ")
		print("|______________")
	elif(guesses == 5):
		print("_______________")
		print("|      |")
		print("|      O")
		print("|     \|/")
		print("|      |")
		print("|     |")
		print("|______________")
	elif(guesses == 6):
		print("_______________")
		print("|      |")
		print("|      O")
		print("|     \|/")
		print("|      |")
		print("|     | |")
		print("|______________")
		print("\n")
		print("The word was %s." %wd)
		print("\n")
		print("\nYou lose! Try again!")
		print("Do you want to play again? Press 1 for yes and 2 for no.")
		again = str(input(">"))
		again = again.lower()
		if again == "1":
			hangman()
		return

		
def selectWord():
	file = open("freq.txt")
	words = file.readlines() 
	myword = 'a'
	while(len(myword) < 4):
		myword = random.choice(words)
		myword = str(myword).strip('[]')
		myword = str(myword).strip("''")
		myword = str(myword).strip("\n")
		myword = str(myword).strip("\r")
	myword = myword.lower()
	return myword

def hangman():
	guesses = 0
	
	word = selectWord() # gives u a random word, say  - hello
	word_list = list(word) # converts hello into a list of character, like = ['h','e','l','l','o']
	
	blanks = "_"*len(word) #print _ (blanks) according to length of word, like for hello it print 5 blanks
	blank_list = list(blanks) #convert blanks into list, like for hello blanks = ['_','_','_','_','_']
	new_blank_list = list(blanks)

	guess_list = []

	print("Lets play the game")
	hang(guesses, word)

	print(' '.join(blank_list))
	print("\n")
	print("Guess a letter: ")

	while guesses < 6:
		guess = str(input())
		guess = guess.lower()

		if len(guess) > 1 : # like u type 'ab'
			print("Stop Cheating. Guess only one letter at a time.")
		elif guess == "": # like you can't type any letter and pressed enter
			print("Don't you want to play? Enter one letter at a time.")
		elif guess in guess_list:
			print("You already guessed that letter! ")
		else:
			guess_list.append(guess)
			i = 0 
			while i < len(word):
				if guess == word[i]:
					new_blank_list[i] = word_list[i]
				i = i+1

			if new_blank_list == blank_list:
				print("Your letter isn't here")
				guesses = guesses+1	
				hang(guesses,word)

				if guesses<6:
					print("Guess again")
					print("".join(blank_list))

			elif word_list != blank_list:
				blank_list = new_blank_list[:]		
				print("".join(blank_list))

				if word_list == blank_list:
					print("You won")
					print("Do you want to play again ? Press 1 for yes and 2 for no.")
					again = str(raw_input("<"))
					if again == "1":
						hangman()
					quit()

				else:
					print("Great guess! Guess another!")
hangman()

	