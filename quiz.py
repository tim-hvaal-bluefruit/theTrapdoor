# make a dict of questions and answers
# intro are you ready to play the quiz?
# use a for loop to ask questions and check the answer
# print total correct
# ask user if they'd like to play again

questions = {
  "what colour is the sky? ": "blue",
  "what colour is grass? ": "green",
  "what colour are bricks? ": "red" }

while True:
  response = input("are you ready to start the quiz? (y/n) ").lower().strip()  #remember these two funcs
  if (response == 'n') or (response == 'no'):
    quit()
  if (response != 'y') and (response != 'yes'):  #handle these cases like this so the rest of func isn't in an if block
    continue

  print()
  print("let's begin! " + '\n')
  count = 0
  for question,answer in questions.items(): #remember how to loop through a dict
    response = input(question).lower()
    if response == answer:
      print("you einstein" + "\n")
      count += 1
    else:
      print("you stoopid!" + "\n")

  print(f"you got {count} / {len(questions)} questions correct")
  replay = input("play again? (y/n) ").lower() #remember input func only expects one parameter (not like print)
  if replay != ('y' or 'yes'):
    break
  print()
