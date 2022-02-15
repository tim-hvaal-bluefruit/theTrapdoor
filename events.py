import items
import locations
import sys


#-------------------------------------------------- USE ------------------------------------------------------#


def use_candle():

    print("  you hold the candle in your hands")


def use_match():

    if items.items["match"]["active"] == False:
        print("  you've used your last match!\n")
        return

    print("\nyou use the match to light the candle, light spills into the room")
    items.items["match"]["description"] = items.MATCH_BURNT
    items.items["match"]["examine"] = items.MATCH_BURNT_EXAMINE
    items.items["match"]["active"] = False
    items.items["candle"]["description"] = items.CANDLE_LIT
    items.items["candle"]["examine"] = items.CANDLE_LIT_EXAMINE
    locations.light_source = True
    locations.chamber["look"] = locations.CHAMBER_TEXT_LIGHT
    locations.chamber["examine"] = locations.CHAMBER_TEXT_EXAMINE_LIGHT
    locations.current_location['checked'] = False
    locations.chamber["room_openable"].append("trapdoor")
    locations.chamber["room_openable"].append("door")
    locations.parlour["room_openable"].append("door")
    locations.chamber["room_items"].append("key")
    locations.chamber["room_items"].append("skull")


def use_key():

    if items.items["key"]["active"] == False:
        print("  you've already unlocked the door")
        return

    print("\nthe key fits into door! You turn the key and open the lock")
    items.doors["door"]["examine"] = items.DOOR1_EXAMINE_OPEN
    items.doors["door"]["active"] = True
    items.items["key"]["active"] = False
    return


def use_crowbar():

    if "trapdoor" not in locations.current_location["room_openable"]:
        print("I can't see anything to use this thing with")
        return

    elif items.items["crowbar"]["active"] == False:
        print("  you've already used the crowbar on the trapdoor")
        return

    print("\nyou manage to prise the trapdoor loose, you should be able to open it now!")
    items.doors["trapdoor"]["active"] = True
    items.items["crowbar"]["active"] = False
    return


def use_knife():

    if "knife" not in items.inv:
        print("I don't seem to have one of those")
        return

    elif (locations.current_location != locations.chamber) or (items.doors["trapdoor"]["count"] != 1):
        print("  i'm not sure what to do with it")
        return

    else:
        print(
            "you try to slash at the beast with the carving knife but you hopelessly miss")


#--------------------------------------------- OPEN / CLOSE ------------------------------------------------#


def open_door():

    print("you push the door open and light from your candle spills into a new room")
    locations.chamber['exits'].append('west')
    locations.chamber['west'] = locations.parlour
    locations.parlour['exits'].append('east')
    locations.parlour['east'] = locations.chamber


def close_door():

    print("you close the door")
    items.doors["door"]["open"] = False


def open_trapdoor():

    print("with an immense effort you lift the trapdoor wide open. You peer into the gloomy depths below")
    items.doors["trapdoor"]["examine"] = items.TRAPDOOR_EXAMINE_ACTIVE
    items.doors["trapdoor"]["open"] = True


def close_trapdoor():

    if items.doors["trapdoor"]["count"] == 1:
        print("you hit the beast on the head - you hear it hit the ground several seconds later")
        items.doors["trapdoor"]["open"] = False
        print("suddenly the human skull starts to speak to you, \"berk, that was a close one! I told you not to open that trapdoor!")
        print("well don't you've won the game!")
        items.doors["trapdoor"]["win"] = True

        # end screen - "thanks for playing"

    else:
        print("you slam the heavy trapdoor with a bang, the strange noises start to recede into the distance")
        items.doors["trapdoor"]["count"] = 7
        items.doors["trapdoor"]["open"] = False
