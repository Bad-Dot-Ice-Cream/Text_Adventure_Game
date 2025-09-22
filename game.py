# adventure.py

#Code for text to print one at a time, cuz its cool   ¯\_(ツ)_/¯
import sys
import time

import sys, time

def typing(text):
    for character in text:
      sys.stdout.write(character)
    sys.stdout.flush()
time.sleep(0.05)

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def slow_type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)

def fast_type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

print("-------------------------------------------------------------")
slow_type("\n=== TEXT ADVENTURE: SECRET BUNKER ===")
slow_type("\nType 'help!' for commands. \n")

# --- game state ---
current_room = "trail"     # starting room
rooms = ["trail", "village", "forest", "bunker", "darkness"]  #flexible list of locations
exits = [
    ["village"],                              # Trail exits into
    ["trail", "forest", "bunker"],            # Village exits into
    ["village", "bunker"],                    # Forest exits into
    ["forest", "darkness"],                   # Bunker exits into
    []                                        # Darkness exits into (nothing, endgame)
]
inventory = []                                # Inventory list, to be expanded during gameplay
turns_left = 30
has_won = False
is_running = True

def show_help():
    fast_type("Commands: search, go <room>, take <item>, use <item>, inv, help, quit.")

def show_room():
    fast_type(f"\nYou are currently at the {current_room}.")
    # Different descriptions based on current location
    if current_room == "trail":
        typing("A dusty old trail, a sign ahead of you says:\n'Welcome to Pine Vill\nQuiet village, quaint people.")
    elif current_room == "village":
        typing("Welcome to Pine Vill, a relatively small community offset from most popular locations, known for it's hospitality and traditional lifestyle.\nPerhaps you can find a vendor and purchase an item for your explorations...")
    elif current_room == "forest":
        typing("A deep forest leading out of Pine Vill with a seemingly ancient path leading somewhere into the distance.\nShadows dance between the trees as you pass and you hear many... questionable sounds around you... Some sound much closer than others..")
    elif current_room == "bunker":
        typing("The path leads to what can only be described as a bunker hidden far into the woods. It's remains decorated with vines, claw marks, and various other signs suggesting of it's age.\nBeneath the surround overgrowth you can vaguely make out several buttons of varying numeric value... perhaps an item could help you clear the debris and so that you may uncover what lies beneath.")
    elif current_room == "darkness":
        typing("A metal stairway leads down into the bunker, even more scratch marks can be seen on the walls and floor. The stairs clang and creak as you approach, groaning under new unexpected weight they hadn't felt for decades...")
    else:
        slow_type("As you gaze into the stillness of the distance you realize how quiet it is...\nToo quiet, one could say...")

def room_index(name):
    #
    for i, r in enumerate(rooms):     # Search helper for clarifying rooms
        if r == name:
            return i
    return -1

def move_player(dest):
    global current_room
    cur_idx = room_index(current_room)
    if cur_idx == -1:
        slow_type("You're feeling isolated and rather lost...")
        return
    if dest in exits[cur_idx]:
        current_room = dest
        show_room()
    else:
        fast_type("You cannot go there from your current location.")

def search_action(rooms):
    if current_room == "trail":
        typing("")

def take_item(item):
    if current_room == "trail" and item == "coins":
        if "coins" not in inventory:
            inventory.append("coins")
            print("You take the scattered coins and add them to your inventory.")
        else:
            print("You already have the coins.")
    else:
        print("You can't take that here.")

def use_item(item):
    global has_won
    if current_room == "bunker" and item == "keypad":
        ans = input("Keypad puzzle: enter the sum of (9 * 4) - 6: ")
        if ans.isidigit() and int(ans) == ((9 * 4) - 6):    # math + conditional
            print("The sliding metal door shutters, shaking violently as it lifts")