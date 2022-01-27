from inventory import items
import inventory
from interaction import actions, doors
import locations
import helpers
from time import sleep

location = locations.chamber

def main():

  while True:
    if location['changed'] == True:
      print(location["look"])
      location['changed'] = False
      sleep(1)

    options_text = helpers.make_options_text()
    user_input = input(options_text).lower().strip()

    input_list = user_input.split(' ')
    first_word = input_list[0]

    keyword = True
    options = helpers.user_options(keyword)
    if (first_word not in options ):
      print("i'm not sure i can do that...")
    if first_word == 'look':
      location['changed'] = True
      continue

    if (first_word == 'inv'):
      check_inventory()
      continue

    if (first_word == 'get'):
      get_thing(input_list)
      continue

    if (first_word == 'use'):
      use_thing(input_list)
      continue


###########################################

def check_inventory():

  print("\n you are carrying:")
  
  for key,value in items.items():
    if value["in_inv"] == True:
      print("  ", value["description"])
  print()


###########################################

def get_thing(input_list):
  
  second_word = input_list[1]

  if location[second_word] not in location:
    print("I don't see one of those")
    return
  
  if location[second_word] != True:
    print("That's not possible")
    return
  
  items[second_word]['in_inv'] == True
  location[second_word] == False


###########################################

def use_thing(input_list):

  global location
  second_word = input_list[1]

  for key, value in items.items():
    
    if second_word != key:
      continue

    if items[second_word]['in_inv'] != True:
      print("you don't have one of those!")
      continue
    
    # candle
    if second_word == 'candle':
      print("  you hold the candle in your hands\n")
      return

    # match
    if second_word == 'match':
      
      if items["match"]["active"] == False:
        print("  you've used your last match!\n")
        return
      
      print("  you use the match to light the candle, light spills into the room\n")
      items["match"]["description"] = inventory.MATCH_BURNT
      items["match"]["examine"] = inventory.MATCH_BURNT_EXAMINE
      items["match"]["active"] = False

      items["candle"]["description"] = inventory.CANDLE_LIT
      items["candle"]["examine"] = inventory.CANDLE_LIT_EXAMINE

      locations.light_source = True
      locations.chamber["look"] = locations.CHAMBER_TEXT_LIGHT

      doors["trapdoor"]["present"] = True
      doors["door"]["present"] = True
      actions["open"]["available"] = True
      location["item"] = ["key"] # got to hear - need a fresh brain
      return
    
    else:
      print("it is forbidden")


if __name__ == '__main__':
  main()