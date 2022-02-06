import items
import locations

#--------------------------------------------------------------------------------- make options

def make_options_text() -> str:

  options_list = make_options_list()
  
  options_text = "\nWhat would you like to do? ("
  for i in options_list:
    options_text += ("'" + i + "'  ")
  options_text += '): '
  return options_text


def make_options_list() ->list[str]:

  options_list = []
  options_list.append('look')
  options_list.append('examine')

  if len(locations.current_location['room_items']) != 0:
    options_list.append('get')

  if len(items.inv) != 0:
    options_list.append('inv')
    options_list.append('use')

  if len(locations.current_location['exits']) != 0:
    for exit in locations.current_location['exits']:
      options_list.append(exit)

  return options_list

#-------------------------------------------------------------------------------- look

def look():

  print(locations.current_location["look"])

  if len(locations.current_location['room_items']) != 0:
    print("you can see...")
    for item in locations.current_location['room_items']:
      print(items.items[item]['description'])

  if len(locations.current_location['exits']) != 0:
    print("you can go ", end='')
    for exit in locations.current_location['exits']:
      print(exit, ' ')

  locations.current_location['checked'] = True

#------------------------------------------------------------------------------- examine

def examine(second_word):

  if (second_word == "room"
          or second_word == locations.current_location["user_text"]):

    if locations.current_location["user_text"] == locations.chamber["user_text"]:
      print(locations.current_location["examine"])

    elif locations.current_location["user_text"] == locations.parlour["user_text"]:
      print(locations.current_location["examine"])

    return

  if (second_word not in items.inv 
          and second_word not in locations.current_location["room_items"] 
          and second_word not in locations.current_location["room_openable"]):

      print("examine what? (hint: you can examine nearby things or items you are carrying)")
      return

  if second_word in items.inv:
    print(items.items[second_word]["examine"])

  elif second_word in locations.current_location["room_items"]:
    print(items.items[second_word]["examine"])
  
  elif second_word in locations.current_location["room_openable"]:
    print(items.doors[second_word]["examine"])

#------------------------------------------------------------------------------- inv

def check_inv():

  if len(items.inv) == 0:
    print("you aren't carrying anything")
    return

  print("\nyou are carrying:")
  for item in items.inv:
    print("  ",items.items[item]["description_inv"])

#------------------------------------------------------------------------------- get

def get_item(second_word):

  if second_word not in locations.current_location['room_items']:
    print("i can't see one of those")
    return

  locations.current_location['room_items'].remove(second_word)
  items.inv.append(second_word)
  print(f"you got the {second_word}!")

#------------------------------------------------------------------------------- move

def move(first_word):

  if first_word not in locations.current_location['exits']:
    print("you can't go that way")
    return

  locations.current_location = locations.current_location[first_word]
  locations.current_location['checked'] = False

#------------------------------------------------------------------------------- use

def use_item(second_word):

  if second_word not in items.inv:
    print("i don't seem to have one of those")
    return

  if second_word == 'candle':
    use_candle()

  elif second_word == 'match':
    use_match()

  elif second_word == 'key':
    use_key()

  else:
    return

#------------------------------------------------------------------------------- use items

def use_candle():
  print("  you hold the candle in your hands")


def use_match():
  if items.items["match"]["active"] == False:
    print("  you've used your last match!\n")
    return
  print("\nyou use the match to light the candle, light spills into the room")
  items.items["match"]["description"] = items.MATCH_BURNT
  items.items["match"]["examine"] = items.MATCH_BURNT_EXAMINE
  items.items["match"]["active"] = False
  items.items["candle"]["description"] = items.CANDLE_LIT
  items.items["candle"]["examine"] = items.CANDLE_LIT_EXAMINE
  locations.light_source = True
  locations.chamber["look"] = locations.CHAMBER_TEXT_LIGHT
  locations.chamber["examine"] = locations.CHAMBER_TEXT_EXAMINE_LIGHT
  locations.current_location['checked'] = False
  locations.chamber["room_openable"].append("trapdoor")
  locations.chamber["room_openable"].append("door")
  locations.chamber["room_items"].append("key")


def use_key():
  if items.items["key"]["active"] == False:
    print("  you've already unlocked the door")
    return
  print("\nthe key fits into door! You turn the key and open the door to a new room!")
  items.doors["door"]["examine"] = items.DOOR1_EXAMINE_OPEN
  locations.chamber['exits'].append('west')
  locations.chamber['west'] = locations.parlour
  locations.parlour['exits'].append('east')
  locations.parlour['east'] = locations.chamber
  items.items["key"]["active"] = False
  return

#-------------------------------------------------------------------------------
