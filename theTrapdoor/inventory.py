#Descriptions
CANDLE = "a small unlit candle"
CANDLE_EXAMINE = "it's on a candlestick so i can carry it around with me"
CANDLE_LIT = "a lit candle on a candleholder"
CANDLE_LIT_EXAMINE = "it's burning dimly in the gloom"

MATCH = "an unlit match in a small grubby box"
MATCH_EXAMINE = "one last match - use it carefully"
MATCH_BURNT = "a burnt match in a grubby box"
MATCH_BURNT_EXAMINE = "it looks like it's useless"

KEY = "a large rusty key hanging on a hook by the door"
KEY_EXAMINE = "it's big and rusty"

items = {
  "candle": 
    {"user_text": "candle", 
    "description": CANDLE,
    "examine": CANDLE_EXAMINE,
    "in_inv": True
    },

  "match": 
    {"user_text": "match",
    "description": MATCH,
    "examine": MATCH_EXAMINE,
    "in_inv": True,
    "active": True
    },

  "key": 
    {"user_text": "key",
    "description": KEY,
    "examine": KEY_EXAMINE,
    "in_inv": False,
    }

}