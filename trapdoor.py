import sys
import locations
import items
import helpers
import events
from PIL import Image 

#-------------------------------------------------- INITIAL GAME STATE ------------------------------------------------------#


locations.current_location = locations.chamber
items.inv = ['match', 'candle']
player_actions = []


#-------------------------------------------------- MAIN LOOP ------------------------------------------------------#


def main():

    print("\nWelcome to the trapdoor")
    print("('h' help, 'q' quit)")

    while True:

        if items.doors["trapdoor"]["open"] == True:
            events.trapdoor()

        if (items.doors["trapdoor"]["win"] == True) or (items.doors["trapdoor"]["lose"] == True):
            pic = Image.open("resources/endScreen.jpg")
            pic.show()
            play_again()

        if locations.current_location['checked'] == False:
            helpers.look()

        # figure out what to ask, and ask player what to do
        options_text = helpers.make_options_text()
        player_answer = input(options_text).lower().strip()

        # parse player answer
        if player_answer == "q":
            sys.exit()
        args = player_answer.split(' ')
        if len(args) > 2:
            continue
        first_word = args[0]
        if len(args) == 2:
            second_word = args[1]
        else:
            second_word = ' '

        # get available actions and compare to player answer
        player_actions = helpers.make_options_list()

        if (first_word not in player_actions):
            print("    i'm not sure i can do that...")

        elif first_word == 'h' or first_word == 'help':
            helpers.help()
        
        elif first_word == 'look':
            locations.current_location['checked'] = False # so look runs next loop

        elif first_word == 'examine':
            helpers.examine(second_word)

        elif (first_word == 'inv'):
            helpers.check_inv()

        elif (first_word == 'open'):
            helpers.open(second_word)

        elif (first_word == 'close'):
            helpers.close(second_word)

        elif first_word in ['west', 'east', 'north', 'south', 'up', 'down']:
            helpers.move(first_word)

        elif first_word == 'get':
            helpers.get_item(second_word)

        elif first_word == 'use':
            helpers.use_item(second_word)

        # finally increment trapdoor counter
        if items.doors["trapdoor"]["open"] == True:
            items.doors["trapdoor"]["count"] -= 1


#-------------------------------------------------- PLAY AGAIN ------------------------------------------------------#


def play_again():

    game_state = input("would you like to play again? (y/n) ").lower().strip()

    if game_state == 'y' or 'yes':
        sys.exit() # should run init func or something
    if game_state == 'n' or 'no':
        sys.exit()


if __name__ == '__main__':
    main()
