# descriptions
CHAMBER_TEXT_DARK ='''
the chamber is cold and dark...'''

CHAMBER_TEXT_LIGHT ='''
the chamber is cold and dark... but after a moment your eyes adjust to the gloom,
you start to make out a large wooden trapdoor in the centre of the room,
beyond that is a small wooden door.'''

CHAMBER_TEXT_EXAMINE ='''
you notice a key and a spider...'''

PARLOUR_TEXT ='''
you are in a parlour...'''

PARLOUR_TEXT_EXTRA ='''
it's a parlour...'''

# logic

light_source = False


parlour = {
  'light': light_source,
  'look': PARLOUR_TEXT,
  'examine': PARLOUR_TEXT_EXTRA,
  'checked': False,
  'room_openable': [],
  'room_items': [],
  'exits': [],
  'east': None
}

chamber = {
  'light': light_source,
  'look': CHAMBER_TEXT_DARK,
  'examine': CHAMBER_TEXT_EXAMINE,
  'checked': False,
  'room_openable': [],
  'room_items': [],
  'exits': [],
  'west': None
}

current_location = None
