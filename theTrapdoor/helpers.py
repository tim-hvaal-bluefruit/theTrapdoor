import theTrapdoor
import inventory
from interaction import actions, doors


def make_options_text():
  text = "What would you like to do? (Type: "
  keyword = False
  for i in user_options(keyword):
    text += ("'" + i + "'  ")
  text += '): '
  return text


def user_options(keyword: bool): #returns available options as text / or as keywords if True
  options_list = []

  # does room have items?
  if theTrapdoor.location['item'] is not None:
    actions['get']['available'] = True

  # does inventory have items in it
  for key, value in inventory.items.items():
    if inventory.items[key]['in_inv'] == True:
      actions['use']['available'] = True
      break

  # does room have things to open
  if theTrapdoor.location['openable'] is not None:
    actions['open']['available'] = True

  # param True ? just return keywords
  if keyword == True:
    for action in actions:
      if actions[action]["available"] == True:
        options_list.append(action)
    return options_list

  # param None then return the text 
  for action in actions:
    if actions[action]["available"] == True:
      options_list.append(actions[action]["display_text"])
  return options_list
