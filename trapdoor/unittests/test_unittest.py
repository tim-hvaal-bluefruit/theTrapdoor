from typing import Match
import helpers
from io import StringIO
import unittest
from unittest.mock import patch

class Test_LookFunction(unittest.TestCase):
 
  def test_look__sets_location_changed_to_false(self):
    
    helpers.look()
    self.assertEqual(helpers.location['changed'], False)

# what if user just types get

  # def test_look_prints_all_items_available(self): 

  #   with patch('sys.stdout', new = StringIO()) as fake_out:
  #     trapdoor.look()
  #     self.assertIn("you can see...\n", fake_out.getvalue())

class Test_user_types_examine_something(unittest.TestCase):
    
  def test_that_when_user_types_examine_then_candle_candle_examine_text_is_printed(self):

      #given
    player_input = "examine candle"

      #when
























# what do i want to test
'''
DECISION TREE
look around
check inventory
use match
    look around
    check inventory
    use candle (already using)
    open trapdoor (locked)
    open door (opens)
        go east (location change to parlour)
            go west

            look (parlour has skull and chopping board)
            inventory
            examine chopping board
                you find a knife
            get skull
            get chopping board (it's nailed down)

  get spider (goes in inventory)
      get key
          open trapdoor(timer starts 5 moves till beast appears)
              close trapdoor (timer stops)
              close trapdoor on 5th move (kills beast)
                  win game

              anything else (6th move beast appears)
              anything (7th move you get clobbered and lose consciousness)
                  start again
        





'''



if __name__ == '__main__':
  unittest.main()