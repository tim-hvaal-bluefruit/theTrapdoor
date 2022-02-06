
#------------------------------------------------------------------------------- general template

NAME = "- "
NAME_INV = "- "
NAME_EXAMINE = ""

#------------------------------------------------------------------------------- chamber descriptions

CANDLE = "- a small unlit candle"
CANDLE_EXAMINE = "it's on a candlestick so i can carry it around with me"
CANDLE_LIT = "- a lit candle on a candleholder"
CANDLE_LIT_EXAMINE = "it's burning dimly in the gloom"

MATCH = "- an unlit match in a small grubby box"
MATCH_EXAMINE = "one last match - use it carefully"
MATCH_BURNT = "- a burnt match in a grubby box"
MATCH_BURNT_EXAMINE = "it looks like it's useless"

KEY = "- a large rusty key hanging on a hook by the door"
KEY_INV = "- a large rusty key"
KEY_EXAMINE = "it's big and rusty"

DOOR1_CHAMBER = "- a small wooden door leading to the west"
DOOR1_PARLOUR = "the door leads back to the chamber to the east"
DOOR1_EXAMINE_LOCKED = "it's locked"
DOOR1_EXAMINE_OPEN = "it's swinging noisily on it's hinges"

TRAPDOOR = "- a huge trapdoor in the ground"
TRAPDOOR_EXAMINE_INACTIVE = "it's very heavy, you can't budge it"
TRAPDOOR_EXAMINE_ACTIVE = "you've opened it wide open - you can't see anything down there but gloom"

#------------------------------------------------------------------------------- parlour descriptions

MEAT_CLEAVER = "- a menacing meat cleaver lying in a pool of blood"
MEAT_CLEAVER_INV = "- a large meat cleaver"
MEAT_CLEAVER_EXAMINE = "i'll chop my leg off with this if i'm not careful"

SKULL = "- a human skull stood upright in an alcove"
SKULL_INV = "- a human skull"
SKULL_EXAMINE = "it feels like it's looking right at you"

SPIDER = "- a huge spider sat in corner of the room"
SPIDER_EXAMINE = "i don't think you can catch it, it's moving around too fast"

CROWBAR = "- a crowbar"
CROWBAR_INV = "- a crowbar"
CROWBAR_EXAMINE = " i could do some damage with this thing"

#------------------------------------------------------------------------------- state

items = {

  'candle': { 
    "description": CANDLE,
    "description_inv": CANDLE,
    "examine": CANDLE_EXAMINE,
    "active": True
  },

  'key': {
    "description": KEY,
    "description_inv": KEY_INV,
    "examine": KEY_EXAMINE,
    "active": True
  },

  'match': {
    "description": MATCH,
    "description_inv": MATCH,
    "examine": MATCH_EXAMINE,
    "active": True
  },

  'crowbar': {
    "description": CROWBAR,
    "description_inv": CROWBAR_INV,
    "examine": CROWBAR_EXAMINE,
    "active": True
  },

  'meat_cleaver': {
    "description": MEAT_CLEAVER,
    "description_inv": MEAT_CLEAVER_INV,
    "examine": MEAT_CLEAVER_EXAMINE,
    "active": True
  },

  'skull': {
    "description": SKULL,
    "description_inv": SKULL_INV,
    "examine": SKULL_EXAMINE,
    "active": True
  },

  'spider': {
    "description": SPIDER,
    "description_inv": SPIDER,
    "examine": SPIDER_EXAMINE,
    "active": True
  },
}

doors = {

  "trapdoor": {
    "description": TRAPDOOR,
    "examine": TRAPDOOR_EXAMINE_INACTIVE,
    "open": False,
    "active": False,
    "count": 5
    },

  "door": {
    "description": DOOR1_CHAMBER,
    "examine": DOOR1_EXAMINE_LOCKED,
    "open": False,
    "active": False
    }
}

inv = []