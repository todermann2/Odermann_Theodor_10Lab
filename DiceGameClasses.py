'''

Theodor Odermann

3/22/24

This program will hold all the Classes for the Dice Game Program. 

'''

import random

class Die:
	def __init__(self, sides):
		self.sides = sides
		self.value = 1
	
	def roll(self):
		self.value = random.randint(1, self.sides)
		
	def getValue(self):
		return self.value
		
	def __str__(self):
		return str(self.value)
		
	def __add__(self, other_die):
		return self.value + other.value
		
	def __gt__(self, other_die):
		return self.value > other.value
	

class Player:
	def __init__(self, name):
		self.name = name
		self.dice = [Die(6), Die(10)]
		
	def rollDice(self):
		for die in self.dice:
			die.roll()
			
	def getDiceValue(self):
		return sum(die.getValue() for die in self.dice)
		
	def __str__(self):
		return self.name
	
	
class HighTwoGame:
	def __init__(self, player1_name, player2_name):
		self.player1 = Player(player1_name)
		self.player2 = Player(player2_name)
		
	def playOneGame(self):
		self.player1.rollDice()
		self.player2.rollDice()
		
		player1_total = self.player1.getDiceValue()
		player2_total = self.player2.getDiceValue()
		
		print(f"{self.player1.name} rolled {player1_total}")
		print(f"{self.player2.name} rolled {player2_total}")
		
		if player1_total > player2_total:
			print(f"{self.player1.name} wins!")
		elif player2_total > player1_total:
			print(f"{self.player2.name} wins!")
		else:
			print("Tie")
			
	def playManyGames(self, num_games):
		
		player1_wins = 0
		player2_wins = 0
		
		for game_outcome in range(num_games):
			self.player1.rollDice()
			self.player2.rollDice()
			
			player1_total = self.player1.getDiceValue()
			player2_total = self.player2.getDiceValue()
			
			player1_sum = self.player1.getDiceValue()
			player2_sum = self.player2.getDiceValue()
			
			if player1_sum > player2_sum:
				player1_wins += 1
			elif player2_sum > player1_sum:
				player2_wins += 1
				
		print(f"The score is {player1_wins} to {player2_wins}")
		if player1_wins > player2_wins:
			print(f"{self.player1.name} wins!")
		elif player2_wins > player1_wins:
			print(f"{self.player2.name} wins!")
		else:
			print("Tie")
			
	
			
		
			
		
	
