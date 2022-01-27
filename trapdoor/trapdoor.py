# ADD NOTES TO NOTION
######################
# CTRL SHFT H vs CTRL H - how to do this in CLion, looks like it looks from the project base, can you specify a subfolder
# bug to fix - picking up items need to change their description
# can't debug because of circular import problem - how to fix
# circular imports problem - dont import main module into others etc
# solved problem of dics containing references to other dicts - has to be set when the item is got
# or could be set with an init method - better
######################

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

    # ask player what to do?
    options_text = helpers.make_options_text()

    # split answer into args
    player_answer = input(options_text).lower().strip()
    args = player_answer.split(' ')

    if len(args) > 2:
      continue

    first_word = args[0]

    if len(args) == 2:
      second_word = args[1]
    else:
      second_word = ' '

    # compare player response to available actions - swap this for a switch statement?
    player_actions = helpers.make_options_list()

    if (first_word not in player_actions):
      print("i'm not sure i can do that...")
      continue
    
    if first_word == 'look':
      locations.current_location['checked'] = False # will run look next loop
      continue

    if first_word == 'examine':
      helpers.examine(second_word)
      continue

    if (first_word == 'inv'):
      helpers.check_inv()
      continue

    if first_word in ['west', 'east', 'north', 'south', 'up', 'down']:
      helpers.move(first_word)
      continue
    
    if first_word == 'get':
      helpers.get_item(second_word)
      continue

    if first_word == 'use':
      helpers.use_item(second_word)
      continue



if __name__ == '__main__':
  main()

