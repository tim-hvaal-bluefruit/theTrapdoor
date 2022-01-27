# descriptions
CHAMBER_TEXT_DARK ='''
the chamber is cold and dark...\n'''

CHAMBER_TEXT_LIGHT ='''
the chamber is cold and dark... but after a moment your eyes adjust to the gloom,
you start to make out a large wooden trapdoor in the centre of the room,
beyond that is a small wooden door.\n'''

CHAMBER_TEXT_EXAMINE ='''
you notice a key and a spider...\n'''

PARLOUR_TEXT ='''
you are in a parlour...\n'''

PARLOUR_TEXT_EXTRA ='''
it's a parlour...\n'''

# logic
light_source = False

chamber = {
  'light': light_source,
  'look': CHAMBER_TEXT_DARK,
  'examine': CHAMBER_TEXT_EXAMINE,
  'openable': None,
  'changed': True,
  'item': None
}

parlour = {
  'light': light_source,
  'look': PARLOUR_TEXT,
  'examine': PARLOUR_TEXT_EXTRA,
  'openable': None,
  'item': None,
  'changed': True
}

