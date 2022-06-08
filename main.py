import random

print ('Hello')

while True:

	print ('Welcome to Rock Paper Sciscors\nPick:\n"R" for "rock"\n"P" for "paper"\n"S" for "scissors"')
	user_input = input ("Pick any of ['R', 'P', 'S']: ").upper()
	rps = ['R', 'P', 'S']
	rpsr = random.choice(rps)

	if user_input == rpsr:
		print ('You chose:', (user_input))
		print ('Computer chose:', (rpsr))
		print ("It is a tie, try again...")

	elif user_input == 'R' and rpsr =='P':
		print ('You chose:', (user_input))
		print ('Computer chose:', (rpsr))
		print ('Paper covers rock, You have lost')
		break

	elif user_input == 'P' and rpsr == 'R':
		print ('You chose:', (user_input))
		print ('Computer chose:', (rpsr))
		print ('Paper covers rock, You have won')
		break
	
	elif user_input == 'S' and rpsr == 'P':
		print ('You chose:', (user_input))
		print ('Computer chose:', (rpsr))
		print ('Scissors cuts paper, You have won')
		break
	
	elif user_input == 'P' and rpsr == 'S':
		print ('You chose:', (user_input))
		print ('Computer chose', (rpsr))
		print ('Scissors cuts paper, You have lost')
		break
	
	elif user_input == 'S' and rpsr == 'R':
		print  ('You chose:', (user_input))
		print ('Computer chose', (rpsr))
		print ('Rock breaks Scissors, you have lost')
		break
	
	elif user_input == 'R' and rpsr == 'S':
		print ('You chose:', (user_input))
		print ('Computer chose', (rpsr))
		print ('Rock breaks Scissors, you have won')
		break
	
	else:
		print ('Invalid input, try again...')