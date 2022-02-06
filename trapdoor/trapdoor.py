import locations
import items
import helpers

# initial game state
locations.current_location = locations.chamber
items.inv = ['match', 'candle']
player_actions = []

def main():
  
  while True:

    if locations.current_location['checked'] == False:
      helpers.look()

    # make options text for debugging 
    options_text = helpers.make_options_text()

    # ask player what to do
    player_answer = input(options_text).lower().strip()
    
    # parse answer to two words
    args = player_answer.split(' ')
    if len(args) > 2:
      continue
    first_word = args[0]
    if len(args) == 2:
      second_word = args[1]
    else:
      second_word = ' '

    # find available actions
    player_actions = helpers.make_options_list()

    # compare available actions to player answer
    if (first_word not in player_actions):
      print("i'm not sure i can do that...")
    
    elif first_word == 'look':
      locations.current_location['checked'] = False # so will run look next loop

    elif first_word == 'examine':
      helpers.examine(second_word)

    elif (first_word == 'inv'):
      helpers.check_inv()

    elif first_word in ['west', 'east', 'north', 'south', 'up', 'down']:
      helpers.move(first_word)
    
    elif first_word == 'get':
      helpers.get_item(second_word)

    elif first_word == 'use':
      helpers.use_item(second_word)


if __name__ == '__main__':
  main()

