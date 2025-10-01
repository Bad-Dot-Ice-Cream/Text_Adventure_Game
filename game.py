# adventure.py

#Code for text to print one at a time, cuz its cool   ¯\_(ツ)_/¯
import sys, time
import string
import random

bunkerLocked = True
cyBattle = False

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    return ""

def slow_type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)
    return ""

def fast_type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    return ""

def random_letters(length=8, speed=0.05):
    chars = string.ascii_uppercase + string.digits + "!@#$%^&*"
    try:
        while True:
            scrambled = "".join(random.choice(chars) for _ in range(length))
            sys.stdout.write("\r" + scrambled)  # overwrite the same line
            sys.stdout.flush()
            time.sleep(speed)
    except KeyboardInterrupt:
        print("\nStopped.")

print("-------------------------------------------------------------")
slow_type("\n=== TEXT ADVENTURE: SECRET BUNKER ===")
fast_type("\nType 'help' for commands. \n")

# --- game state ---
current_room = "trail"     # starting room
rooms = ["trail", "village", "forest", "bunker", "darkness"]  #flexible list of locations
# The exits for each location.   If I'm currently in ______, I can go to...
trail_exits = ["village"]
village_exits = ["trail", "forest"]
forest_exits = ["trail", "village", "bunker"]
bunker_exits = ["village", "forest"]
dark_exits = []

inventory = []                                # Inventory list, to be expanded during gameplay
turns_left = 30
has_won = False
is_running = True

def alwaysShow_Rooms():
    if current_room == "trail":
        print("You are currently at the {current_room}, you may go to the {trail_exits} from here.")
    if current_room == "village":
        print("You are currently at the {current_room}, you may go to the {village_exits} from here.")
    if current_room == "forest":
        print("You are currently at the {current_room}, you may go to the {forest_exits} from here.")
    if current_room == "bunker":
        print("You are currently at the {current_room}, you may go to the {bunker_exits} from here.")
    if current_room == "darkness":
        print(f"You are currently at the {current_room}, you may go to the {random_letters(length=10, speed=0.3)} from here.")

def show_help():
    fast_type("Commands: search, go <room>, use <item>, rooms, inv, help, quit.")

def show_room():
    fast_type(f"\nYou are currently at the {current_room}.")
    # Different descriptions based on current location
    if current_room == "trail":
        typing(" A dusty old trail, a sign ahead of you says:\n'Welcome to Pine Vill\nQuiet village, quaint people.'")
    elif current_room == "village":
        typing(" Welcome to Pine Vill, a relatively small community offset from most popular locations, known for it's hospitality and traditional lifestyle.\nPerhaps you can find a vendor and purchase an item for your explorations...")
    elif current_room == "forest":
        typing(" A deep forest leading out of Pine Vill with a seemingly ancient path leading somewhere into the distance.\nShadows dance between the trees as you pass and you hear many... questionable sounds around you... Some sound much closer than others..")
    elif current_room == "bunker":
        typing(" The path leads to what can only be described as a bunker hidden far into the woods. It's remains decorated with vines, claw marks, and various other signs suggesting of it's age.\nBeneath the surrounding overgrowth you can vaguely make out several buttons of varying numeric value... perhaps an item could help you clear the debris so that you may uncover what lies beneath.")
    elif current_room == "darkness":
        typing(" A metal stairway leads down into the bunker, even more scratch marks can be seen on the walls and floor. The stairs clang and creak as you approach, groaning under new unexpected weight they hadn't felt for decades...")
    else:
        slow_type(" As you gaze into the stillness of the distance you realize how quiet it is...\nToo quiet, one could say...")

def search_room():
    if current_room == "trail":
        typing("You pace yourself as you follow the trail, finding an abundance of spilled coins varying in cleanliness. You find six total.")
        add_coins = input(typing(" Would you like to take the coins?\nY or N: "))
        if add_coins == "Y":
            fast_type(" You decide to take the coins, adding them to your inventory.")
            inventory.append("coins")
        if add_coins == "N":
            fast_type("You choose against taking the coins.")

    elif current_room == "village":
        typing("You see a figure in the distance, bordering the forest. Their arms stand outstretched, resembling a scarecrow...\nYou feel uneasy witnessing this...\nYou can make out large woooden establishment a short ways away from you. Large words above the entrance say, 'Jack's Joyful Shop'.")
        enterShopYN = input(slow_type("\nDo you enter? Y or N: "))
        if enterShopYN == "Y":
            rooms.append("Jack's Shop")
        if enterShopYN == "N":
            print("You decide not to enter. Perhaps you can revisit this location in the future if you ever need something.")
        if enterShopYN != "Y" or "N":
            typing("Please state 'Y' or 'N'")
    
    elif current_room == "forest":
        typing("A figure stands only a matter of feet from your position, arms outstretched. They wear a dark cloak and seem to be muttering indiscernibly to themselves, possibly unaware of your presence.")
        # Cyruss battle initiation or denial
        cyrussInteract = input(slow_type("Do you interact with them or leave them be? Y or N: "))
        if cyrussInteract == "Y":
            fast_type("As you take a few steps in their direction, their head unexpectedly snaps to meet yours. They raise their arms higher and their face becomes visible.")
            cyBattle = True
        if cyrussInteract == "N":
            fast_type("You decide to avoid the strange figure for the time being.\nProbably a wise decision in retrospect.")
        if cyrussInteract != "Y" or "N":
            typing("Please state 'Y' or 'N'")
    elif current_room == "bunker":
        typing("Scouting the surroundings, you notice the ground is layered in rocks covering what remains of the path leading to the metal door of the bunker. Do you take one?")
        take_rock = input(fast_type("Y or N: "))
        if take_rock == "N":
            show_room()
        if take_rock == "Y":
            slow_type("A completely average rock. You could probably try to sharpen it against a nearby tree.")
            slow_type("Average Rock has been added to your inventory.")
            sharpenRock = input(typing("Would you like to attempt to sharpen the rock on a nearby tree? Y or N "))
            if sharpenRock == "Y":
             rock_sub = int(input(fast_type("Rock puzzle: what is the result of (5^2) - 5?")))
            rock_ans = 20
            if rock_sub == "20":
                fast_type("You are successful! Sharpened Rock has been added to your inventory.")
            if rock_sub != "20":
                rock_again = typing("Your attempt to sharpen the rock fails. Would you like to try again? Y or N: ")
                if rock_again == "Y":
                    rock_sub = int(input(fast_type("Rock puzzle: what is the result of (5^2) - 5?")))
                if rock_again == "N":
                    show_room()
        else:
            return print("error")

    elif current_room == "Jack's Shop":
        typing("A bell rings as you enter, with the noticeably handsome shopkeep rising from to the register to answer the call.\n'Hello! Weclome to Jack's Joyful Shop! How can I help you today?'")
        if "coins" not in inventory:
            typing("You do not have enough money to purchase anything here.")
            
        if "coins" in inventory:   
            slow_type("There are various items for purchase:\n$6 Flashlight\n$8 Pocket Knife\n$15 Backpack\n And more, though they extend further and further from your limited amount of pocket-money.")
            purchaseItem = input(typing("The shopkeep asks you if you would like to purchase anything in particular today, a cheerful smile brightening their face. "))
            if purchaseItem == "Flashlight":
                buyFlash = input(typing("Would you like to buy the Flashlight for six coins? Y or N: "))
                if buyFlash == "Y":
                    typing("You trade your coins for a Flashlight. Strong, durable, you feel as though you can place your trust in the glow of its beam. It's even got a little bit of weight to it.")
                    slow_type("Flashlight has been added to your inventory.")
                    inventory.append("Flashlight")
                if buyFlash == "N":
                    typing("You decide not to purchase the Flashlight.")
            if purchaseItem == "Pocket Knife":
                fast_type("Unfortunately, you do not have enough money to purchase that item.")
            if purchaseItem == "Backpack":
                fast_type("Unfortunately, you do not have enough money to purchase that item.")
            if purchaseItem != "Flashlight" or "Pocket Knife" or "Backpack":
                fast_type("You are unable to purchase... that. The shopkeeper gives you a strange, confused look.")



def room_index(name):
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
    if dest in [cur_idx]:
        current_room = dest
        show_room()
    else:
        fast_type("You cannot go there from your current location.")

def use_item(item):
    global has_won
    if current_room == "bunker" and item == "keypad":
        ans = input("Keypad puzzle: enter the sum of (9 * 4) - 6: ")
        if ans.isdigit() and int(ans) == ((9 * 4) - 6):    # math + conditional
            print("The sliding metal door shutters, shaking violently as it lifts.\nThe scent of rust fills your lungs as you gaze into the abyss before you..")
            # adding the darkness to the bunker exits (list method)
            b_idx = room_index("bunker")
            if "darkness" not in [b_idx]:
                [b_idx].append("darkness")
            
        else:
            print("Incorrect. The kepad beeps angrily and flashes red.")
    elif current_room == "darkness" and item == "flashlight":
        if "flashlight" in inventory:
            print("With your trusty flashlight in hand, you prepare yourself to venture further into the forgotten bunker... and perhaps you will find the answers you seek...\nOr perhaps your disappearence will only raise more questions for those outside..\n You win! Thanks for playing  :D")
            has_won = True
        else:
            print("You need something to find your way through the immense darkness.")
    else:
        print("That item cannot be used here.")
    
def handle_command(cmd):
    parts = cmd.strip().lower().split()
    if not parts:
        return
    if parts[0] == "help":
        show_help()
    elif parts[0] == "search":
        search_room()
    elif parts[0] == "go" and len(parts) >= 2:
        move_player(parts[1])
    elif parts[0] == "take" and len(parts) >= 2:
        use_item(parts[1])
    elif parts[0] == "rooms":
        print(rooms)
    elif parts[0] =="inv":
        print("Inventory:", inventory if inventory else "(empty)")
    elif parts[0] == "quit":
        global is_running
        is_running = False
    else:
        print("Unknown command. Type 'help'.")

# --- main loop ---
show_room()
while is_running and not has_won:
    # optional pressure mechanic
    turns_left -= 1
    if turns_left <= 0:
        print("\nYou suddenly fall, clawing at the air as your vision blurs and you fail to pick yourself up. Your chest grows heavy as you begin to lose consciousness..\n You will never find the answers you seek... and your disappearence will only raise more questions for others.\nYou lose.")
        print("||| GAME OVER |||")
        break

    cmd = input("\n> ")
    handle_command(cmd)

if has_won:
    print("\n You are successful! Thanks for playing!")


#--- Shop keep ---
if current_room == "village":
    print("\nYou can make out large woooden establishment a short ways away from you. Large words above the entrance say, 'Jack's Joyful Shop'.")
    enterShopYN = input("\nDo you enter? Y or N: ")
if enterShopYN == "Y":
    rooms.append("Jack's Shop")
if enterShopYN == "N":
    print("You decide not to enter. Perhaps you can revisit this location in the future if you ever need something.")
if enterShopYN != "Y" or "N":
    typing("Please state 'Y' or 'N'")