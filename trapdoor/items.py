#------------------------------------------------------------------------------- descriptions

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
  }
}

doors = {

  "trapdoor": {
    "description": TRAPDOOR,
    "examine": TRAPDOOR_EXAMINE_INACTIVE,
    "open": False,
    "active": False
    },

  "door": {
    "description": DOOR1_CHAMBER,
    "examine": DOOR1_EXAMINE_LOCKED,
    "open": False,
    "active": False
    }
}

inv = []