import sys
import locations
import items
import helpers
import events


#-------------------------------------------------- INITIAL GAME STATE ------------------------------------------------------#


locations.current_location = locations.chamber
items.inv = ['match', 'candle']
player_actions = []


#-------------------------------------------------- MAIN LOOP ------------------------------------------------------#


def main():

    while True:

        if items.doors["trapdoor"]["open"] == True:
            trapdoor()

        if locations.current_location['checked'] == False:
            helpers.look()

        # show options - DEBUG
        options_text = helpers.make_options_text()

        # ask player what to do
        player_answer = input(options_text).lower().strip()

        # quick quit - DEBUG
        if player_answer == "q":
            sys.exit()

        # parse answer to two words
        args = player_answer.split(' ')
        if len(args) > 2:
            continue
        first_word = args[0]
        if len(args) == 2:
            second_word = args[1]
        else:
            second_word = ' '

        # find available actions
        player_actions = helpers.make_options_list()

        # compare available actions to player answer
        if (first_word not in player_actions):
            print("i'm not sure i can do that...")

        elif first_word == 'look':
            # so will run look next loop
            locations.current_location['checked'] = False

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
        
        if items.doors["trapdoor"]["open"] == True:
            items.doors["trapdoor"]["count"] -= 1
        
        if items.doors["trapdoor"]["win"] == True:
            play_again()


#-------------------------------------------------- TRAPDOOR EVENT ------------------------------------------------------#


def trapdoor():
    if items.doors["trapdoor"]["count"] == 6:
        print("\nyou can hear a distant rumbling under ground...")

    elif items.doors["trapdoor"]["count"] == 5:
        print("\nit sounds like giant footsteps...")

    elif items.doors["trapdoor"]["count"] == 4:
        print("\nit's getting louder and much closer...")

    elif items.doors["trapdoor"]["count"] == 3:
        print("\nsomething large is drawing near...")

    elif items.doors["trapdoor"]["count"] == 2:
        print("\nsuddenly everything has gone very quiet... ")

    elif items.doors["trapdoor"]["count"] == 1:

        if locations.current_location == locations.chamber:
            print("\nyou look down to see an enormous pair of eyes staring at you and a grotesque head emerge above the level of the floor, what will you do?!")

        if locations.current_location == locations.parlour:
            print("\nyou hold you're breath, something is crawling into the next room")

    else:  # count is 0

        if locations.current_location == locations.parlour and items.doors["door"] == "closed":
            print("\na huge beast smashes straight through the wooden door and dashes towards you. It grabs you in it's hand and drags you back into the trapdoor")

        print("\na large hand appears and drags you towards the trapdoor, you try to hang on but the beast drags you down into the depths")
        play_again()


#-------------------------------------------------- PLAY AGAIN ------------------------------------------------------#


def play_again():
    game_state = input(
        "would you like to play again? (y/n) ").lower().strip()
    if game_state == 'y' or 'yes':
        pass
    if game_state == 'n' or 'no':
        sys.exit()


if __name__ == '__main__':
    main()
