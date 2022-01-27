import items
import locations


def make_options_text() -> str:

  options_text = "\nWhat would you like to do? ("

  for i in make_options_list():
    options_text += ("'" + i + "'  ")

  options_text += '): '
  return options_text



def make_options_list() ->list[str]:

  options_list = []
  options_list.append('look')

  if len(locations.current_location['room_items']) != 0:
    options_list.append('get')

  if len(items.inv) != 0:
    options_list.append('inv')
    options_list.append('use')

  if len(locations.current_location['room_openable']) != 0:
    options_list.append('open')
  
  if len(locations.current_location['exits']) != 0:
    for exit in locations.current_location['exits']:
      options_list.append(exit)

  return options_list


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



def examine(second_word):

  if second_word not in items.inv:
    "i can't examine that from here"
    return

  locations.current_location['room_items'].remove(second_word)
  items.inv.append(second_word)
  print(f"you got the {second_word}!")



def check_inv():

  if len(items.inv) == 0:
    print("you aren't carrying anything")
    return

  print("\nyou are carrying:")

  for item in items.inv:
    print("  ",items.items[item]["description"])

  return



def get_item(second_word):

  if second_word not in locations.current_location['room_items']:
    "i can't see one of those"
    return

  locations.current_location['room_items'].remove(second_word)
  items.inv.append(second_word)
  print(f"you got the {second_word}!")



def move(first_word):

  if first_word not in locations.current_location['exits']:
    print("you can't go that way")

  locations.current_location = locations.current_location[first_word]
  locations.current_location['checked'] = False


def use_item(second_word):

  if second_word not in items.inv:
    "i don't seem to have one of those"
    return

  for item in items.inv:
    
    if second_word == 'candle':

      print("  you hold the candle in your hands")
      return

    if second_word == 'match':

      if items.items[second_word]["active"] == False:
        print("  you've used your last match!\n")
        return

      print("\nyou use the match to light the candle, light spills into the room")
      items.items["match"]["description"] = items.MATCH_BURNT
      items.items["match"]["examine"] = items.MATCH_BURNT_EXAMINE
      items.items["match"]["active"] = False

      # refactor this ? this is what happens when light source is true
      items.items["candle"]["description"] = items.CANDLE_LIT
      items.items["candle"]["examine"] = items.CANDLE_LIT_EXAMINE

      locations.light_source = True
      locations.chamber["look"] = locations.CHAMBER_TEXT_LIGHT
      locations.current_location['checked'] = False
      locations.chamber["room_openable"].append("trapdoor")
      locations.chamber["room_openable"].append("door")
      locations.chamber["room_items"].append("key")
      return

    if second_word == 'key':

      if items.items[second_word]["active"] == False:
        print("  you've already opened the door")
        return

      print("\nthe key fits into door! You turn the key and open the door to a new room!")
      items.items[second_word]["active"] = False
      items.doors["door"]["examine"] = items.DOOR_EXAMINE_OPEN
      locations.chamber['exits'].append('west')
      locations.chamber['west'] = locations.parlour
      locations.parlour['exits'].append('east')
      locations.parlour['east'] = locations.chamber
      return

  return
