#------------------------------------------------------------------------------- descriptions

CHAMBER_TEXT_DARK ='''
the chamber is cold and dark...'''

CHAMBER_TEXT_LIGHT ='''
the chamber is cold and dark... but after a moment your eyes adjust to the gloom,
you start to make out a large wooden trapdoor in the centre of the room,
beyond that is a small wooden door.'''

CHAMBER_TEXT_EXAMINE_DARK ='''
it's dark and cold, but your footsteps echo as you walk on the stone floor'''

CHAMBER_TEXT_EXAMINE_LIGHT ='''
it's a large chamber with stone walls, it's so cold you can see you're breath'''

PARLOUR_TEXT ='''
you are in a parlour...'''

PARLOUR_TEXT_EXAMINE ='''
it's a large stone room, there are surfaces for preparing food...'''


#------------------------------------------------------------------------------- state

light_source = False

parlour = {
  'user_text': "parlour",
  'light': light_source,
  'look': PARLOUR_TEXT,
  'examine': PARLOUR_TEXT_EXAMINE,
  'checked': False,
  'room_openable': [],
  'room_items': [],
  'exits': [],
  'east': None
}

chamber = {
  'user_text': "chamber",
  'light': light_source,
  'look': CHAMBER_TEXT_DARK,
  'examine': CHAMBER_TEXT_EXAMINE_DARK,
  'checked': False,
  'room_openable': [],
  'room_items': [],
  'exits': [],
  'west': None
}

current_location = None
