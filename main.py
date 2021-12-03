import random, time, os
def main():
	print("Welcome to Rock Paper Scissors")
	time.sleep(1)
	norep = input("Enter to continue")
	playGame = True
	botscore = 0
	userscore = 0
	if playGame:
		while True: 
			time.sleep(1)
			for x in range (0,3):
				cI = random.randint(1,3)
			if (cI == 1):
				cpuChoice = "Rock"
				userChoice = input("Rock, Paper or Scissors")
				if (userChoice == "rock" or userChoice == "Rock"):
					print("")
					print("You chose Rock")
					print("Opponent chose Rock")
					time.sleep(2)
					print("You tied")
				if (userChoice == "paper" or userChoice == "Paper"):
					print("")
					print("You chose Paper")
					print("Opponent chose Rock")
					time.sleep(2)
					print("You won")
					userscore = userscore + 1
				if (userChoice == "scissors" or userChoice == "Scissors"):
					print("")
					print("You chose Scissors")
					print("Opponent chose Rock")
					time.sleep(2)
					print("You lost.")
					botscore = botscore + 1

			if (cI == 2):
				cpuChoice = "Paper"
				userChoice = input("Rock, Paper or Scissors")
				if (userChoice == "rock" or userChoice == "Rock"):
					print("")
					print("You chose Rock")
					print("Opponent chose Paper")
					time.sleep(2)
					print("You lost")
					botscore = botscore + 1
				if (userChoice == "paper" or userChoice == "Paper"):
					print("")
					print("You chose Paper")
					print("Opponent chose Paper")
					time.sleep(2)
					print("You tied")
				if (userChoice == "scissors" or userChoice == "Scissors"):
					print("")
					print("You chose Scissors")
					print("Opponent chose Paper")
					time.sleep(2)
					print("You won")
					userscore = userscore + 1


			if (cI == 3):
				cpuChoice = "Scissors"
				userChoice = input("Rock, Paper or Scissors")
				if (userChoice == "rock" or userChoice == "Rock"):
					print("")
					print("You chose Rock")
					print("Opponent chose Scissors")
					time.sleep(2)
					print("You won")
					userscore = userscore + 1
				if (userChoice == "paper" or userChoice == "Paper"):
					print("")
					print("You chose Paper")
					print("Opponent chose Scissors")
					time.sleep(2)
					print("You lost")
					botscore = botscore + 1
				if (userChoice == "scissors" or userChoice == "Scissors"):
					print("")
					print("You chose Scissors")
					print("Opponent chose Scissors")
					time.sleep(2)
					print("You tied")
			print("Leaderboard")
			print("Your score: " + str(userscore))
			print("Opponent score: " + str(botscore))
			keepPlaying = input("Do you want to play again? y/n")
			if keepPlaying == "y":
				 
				playGame = True
			else:
				print("Okay bye")
				playGame = False
				break
main()