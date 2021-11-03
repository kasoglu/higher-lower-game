from art import logo,gameover,vs
from game_data import data
from replit import clear
import random

#Function generates random account from data.
def generate_random_data():
  """Get data from random account"""
  return random.choice(data)

def format_account(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def compare_data(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def play_game():
  print(logo)
  score = 0
  game_should_continue = True
  print("Welcome to Higher&Lower Game..\n")
  account_a = generate_random_data()
  account_b = generate_random_data()

  #Game will continue unless user guess wrong. And change second data with new one.
  while game_should_continue:
    account_a = account_b
    account_b = generate_random_data()

    while account_a == account_b:
      account_b = generate_random_data()

    print(f"Compare A: {format_account(account_a)} ")
    print(vs)
    print(f"Compare B: {format_account(account_b)} \n")
    #Take user's guess and put the function to check is it correct.
    guess = input("Do you think who has more followers on Instagram? \n Type 'A' or 'B' ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = compare_data(guess, a_follower_count, b_follower_count)
    print(guess)

    clear()
    print(logo)
    
    #Checks if guess is correct increase score and keep continue. Else, finish the game.
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      clear()
      print(gameover)
      print(f"Sorry, that's wrong. Your final score: {score}")
  

while input("Type enter to start new game. ") == "":
  clear()
  play_game()
