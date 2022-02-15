import sys
import items
import locations
import events


#-------------------------------------------------- MAKE OPTIONS ------------------------------------------------------#


def make_options_text() -> str:

    options_list = make_options_list()

    options_text = "\nWhat would you like to do? ("
    for i in options_list:
        options_text += ("'" + i + "'  ")
    options_text += '): '
    return options_text


def make_options_list() -> list[str]:

    options_list = []
    options_list.append('look')
    options_list.append('examine')

    if len(locations.current_location['room_items']) != 0:
        options_list.append('get')

    if len(locations.current_location['room_openable']) != 0:
        options_list.append('open')
        options_list.append('close')

    if len(items.inv) != 0:
        options_list.append('inv')
        options_list.append('use')

    if len(locations.current_location['exits']) != 0:
        for exit in locations.current_location['exits']:
            options_list.append(exit)

    return options_list


#-------------------------------------------------- LOOK ------------------------------------------------------#


def look():

    print(locations.current_location["look"])

    if len(locations.current_location['room_items']) != 0:
        print("you can see...")
        for item in locations.current_location['room_items']:
            print(items.items[item]['description'])

    if len(locations.current_location['exits']) != 0:
        print("you can go ", end='')
        for exit in locations.current_location['exits']:
            print(exit, ' ')

    locations.current_location['checked'] = True


#-------------------------------------------------- EXAMINE ------------------------------------------------------#


def examine(second_word):

    if (second_word == "room"
            or second_word == locations.current_location["user_text"]):

        if locations.current_location["user_text"] == locations.chamber["user_text"]:
            print(locations.current_location["examine"])

        elif locations.current_location["user_text"] == locations.parlour["user_text"]:
            print(locations.current_location["examine"])

        return

    if (second_word not in items.inv
            and second_word not in locations.current_location["room_items"]
            and second_word not in locations.current_location["room_openable"]):

        print(
            "examine what? (hint: you can examine nearby things or items you are carrying)")
        return

    if second_word in items.inv:
        print(items.items[second_word]["examine"])

    elif second_word in locations.current_location["room_items"]:
        print(items.items[second_word]["examine"])

    elif second_word in locations.current_location["room_openable"]:
        print(items.doors[second_word]["examine"])


#-------------------------------------------------- INV ------------------------------------------------------#


def check_inv():

    if len(items.inv) == 0:
        print("you aren't carrying anything")
        return

    print("\nyou are carrying:")
    for item in items.inv:
        print("  ", items.items[item]["description_inv"])


#-------------------------------------------------- OPEN ------------------------------------------------------#


def open(second_word):

    if second_word not in locations.current_location['room_openable']:
        print("i'm not sure i can open that")
        return

    if items.doors[second_word]["active"] == False:
        print(items.doors[second_word]["examine"])
        return

    if items.doors[second_word]["open"] == True:
        print("looks like it's already open")
        return

    if second_word == "trapdoor":
        pass
        events.open_trapdoor()

    if second_word == "door":
        pass
        events.open_door()


#-------------------------------------------------- CLOSE ------------------------------------------------------#


def close(second_word):

    if second_word not in locations.current_location['room_openable']:
        print("i'm not sure i can close that")

    elif items.doors[second_word]["active"] == False:
        print("it's already closed and you can't open it")

    elif items.doors[second_word]["open"] == False:
        print("it's already closed")
        return

    if second_word == "trapdoor":
        events.close_trapdoor()

    elif second_word == "door":
        events.close_door()


#-------------------------------------------------- GET ------------------------------------------------------#


def get_item(second_word):

    if second_word not in locations.current_location['room_items']:
        print("i can't see one of those")
        return

    if second_word == "spider":
        print(items.items["spider"]["examine"])
        return

    locations.current_location['room_items'].remove(second_word)
    items.inv.append(second_word)
    print(f"you got the {second_word}!")


#-------------------------------------------------- MOVE ------------------------------------------------------#


def move(first_word):

    if first_word not in locations.current_location['exits']:
        print("you can't go that way")
        return

    locations.current_location = locations.current_location[first_word]
    locations.current_location['checked'] = False


#-------------------------------------------------- USE ------------------------------------------------------#


def use_item(second_word):

    if second_word not in items.inv:
        print("i don't seem to have one of those")
        return

    if second_word == 'candle':
        events.use_candle()

    elif second_word == 'match':
        events.use_match()

    elif second_word == 'key':
        events.use_key()

    elif second_word == 'crowbar':
        events.use_crowbar()

    elif second_word == 'knife':
        events.use_knife()

    else:
        return
