from typing import Match
import helpers
import locations
from io import StringIO
import unittest
from unittest.mock import patch

class Test_LookFunction(unittest.TestCase):
 
  def test_that_look__sets_location_checked_to_false(self):
    
    locations.current_location = locations.chamber
    helpers.look()
    self.assertEqual(locations.current_location['checked'], True)
























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