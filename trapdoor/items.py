# descriptions
CANDLE = "- a small unlit candle"
CANDLE_EXAMINE = "it's on a candlestick so i can carry it around with me"
CANDLE_LIT = "- a lit candle on a candleholder"
CANDLE_LIT_EXAMINE = "it's burning dimly in the gloom"

MATCH = "- an unlit match in a small grubby box"
MATCH_EXAMINE = "one last match - use it carefully"
MATCH_BURNT = "- a burnt match in a grubby box"
MATCH_BURNT_EXAMINE = "it looks like it's useless"

KEY = "- a large rusty key"
KEY_IN_SITU = "- a large rusty key hanging on a hook by the door"
KEY_EXAMINE = "it's big and rusty"

DOOR = "- a small wooden door leading to the west"
DOOR_PARLOUR = "the door leads back to the chamber to the east"
DOOR_EXAMINE_LOCKED = "it's locked"
DOOR_EXAMINE_OPEN = "it's swinging noisily on it's hinges"

TRAPDOOR = "- a huge trapdoor in the ground"
TRAPDOOR_EXAMINE_INACTIVE = "it's very heavy, you can't budge it"


items = {

  'candle': {
    "user_text": "candle", 
    "description": CANDLE,
    "examine": CANDLE_EXAMINE,
    },

  'match': {
    "user_text": "match",
    "description": MATCH,
    "examine": MATCH_EXAMINE,
    "active": True
    },

  'key': {
    "user_text": "key",
    "description": KEY_IN_SITU,
    "examine": KEY_EXAMINE,
    "active": True
    }
}

doors = {

  "trapdoor": {
    "open": False,
    "description": TRAPDOOR,
    "examine": TRAPDOOR_EXAMINE_INACTIVE
    },

  "door": {
    "open": False,
    "description": DOOR,
    "examine": DOOR_EXAMINE_LOCKED
    }
}

inv = []