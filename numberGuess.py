 # get user to pick top of range
 # check it's a number
 # generate a random number using top of range
 # continually ask for a number
 # check it's a number
 # if it's right return number of guesses
 # if it's wrong ask question again

import random

while True:
  range_top = input("welcome to the number guesser! Pick a number below 20: ")
  if (range_top.isdigit() == False): #remember how to check if it's a digit
    continue
  range_top = int(range_top)
  rand = random.randint(1, range_top) #remember subtlety between randint and randrange
  break

num_guesses = 0
print(f"a random number has been generated betwen 0 and {range_top}")
while True:
  guess = input("guess the random number? ")
  if guess.isdigit() == False:
    print("not a number")
    continue
  num_guesses += 1
  guess = int(guess)
  if guess == rand:
    break
  else:
    if guess > rand:
      print("over")
    if guess < rand:
      print("under")
    continue

print("you got the answer right after", num_guesses, "guess(es)")