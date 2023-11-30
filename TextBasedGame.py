import sys
import re

# Constants:
START_ROOM = 'Time Headquarters'


# Intro Class:
class TitleIntro:
    def __init__(self):
        self.title = "  Temporal Odyssey: Guardians of the Continuum  "
        self.owner = "  By: Cameron Soller  "
        self.story_background = """
            In the epoch of 2341, an organization known as "The Keepers" has been entrusted with the formidable 
            responsibility of safeguarding the temporal continuum from malevolent forces. Following a pivotal 
            breakthrough in temporal technology subsequent to the 21st century, a revolutionary device emerged, 
            endowed with the unprecedented capability to navigate seamlessly through the dimensions of time and space. 
            At the forefront of this critical mission stands none other than yourself – the apex operative within 
            The Keepers, armed with the pinnacle of temporal advancement, the time-traveling device. 
            As the vanguard of this cutting-edge technology, you bear the pivotal role in upholding the sanctity of 
            the timeline and thwarting the nefarious threats that jeopardize the very fabric of existence.
        """

    def display_welcome_text(self):
        # Create a box around title
        title_box = f"+{'=' * (len(self.title) + 4)}+"

        # Print the box and content
        print(title_box)
        print(f"| {self.title}   |")
        print(title_box)

        # print owner
        print(f"  {self.owner}")
        print(f"{'_' * (len(self.title) + 6)}")

        # Print the story background
        print(self.story_background)


# Functions
def display_room_with_border(room_name):
    border_length = len(room_name) + 4  # Adjusting for borders
    print("_" * border_length)
    print(f"| {room_name} |")
    print("_" * border_length)


def move_through_portal(destination_room):
    display_room_with_border(destination_room)
    print(f"A PORTAL OPENS AND YOU ENTER THE PORTAL\nYou are now in the {destination_room}")


def press_enter_to_continue():
    # Enter to Continue Story Prompt
    user_input = input("Press ENTER to continue\n...or type 'E' to exit: ")
    if user_input == '':
        print()
        return True  # Continue the game
    elif user_input.upper() == 'E':
        print("Exiting the game.")
        sys.exit()  # Exit the entire program
    else:
        print("** Invalid input. Please try again. **")
        print()
        return press_enter_to_continue()  # Recursive call for re-entering input


def game_over():
    print("Game Over! Thanks for playing.")
    sys.exit()


# Game Play Class
class StartJourney:
    def __init__(self):
        self.rooms = {
            'Time Headquarters': {'Renaissance Library': 'North', 'Medieval Castle Dungeon': 'East',
                                  'Futuristic Laboratory': 'South', 'World War II Bunker': 'West'},
            'Renaissance Library': {'Time Headquarters': 'South', 'Ancient Pyramid Chamber': 'East'},
            'Ancient Pyramid Chamber': {'Renaissance Library': 'West'},
            'World War II Bunker': {'Time Headquarters': 'East', 'Space Age Observatory': 'South'},
            'Space Age Observatory': {'World War II Bunker': 'North'},
            'Futuristic Laboratory': {'Time Headquarters': 'North', 'Victorian Era Parlor': 'East'},
            'Victorian Era Parlor': {'Futuristic Laboratory': 'West'},
            'Medieval Castle Dungeon': {'Time Headquarters': 'West', 'Prehistoric Cave': 'North'},
            'Prehistoric Cave': {'Medieval Castle Dungeon': 'West'}
        }

        self.items = {
            'Time Headquarters': None,
            'Renaissance Library': 'Amulet of blood',
            'Ancient Pyramid Chamber': 'Mask of Tutankhamun',
            'World War II Bunker': 'Compass',
            'Space Age Observatory': 'Astronaut Gloves',
            'Futuristic Laboratory': 'Sonic Screwdriver',
            'Victorian Era Parlor': 'Tiara',
            'Medieval Castle Dungeon': 'Rusted Key',
            'Prehistoric Cave': None
        }

        self.descriptions = {
            'Time Headquarters': "The central hub for timekeepers. It's filled with advanced technology and monitors "
                                 "displaying temporal anomalies.",
            'Renaissance Library': 'A vast library containing knowledge from the Renaissance era. Books and scrolls '
                                   'line the shelves.',
            'Ancient Pyramid Chamber': 'A mysterious chamber within an ancient pyramid. Hieroglyphics cover the walls.',
            'World War II Bunker': 'A bunker from the World War II era, equipped with maps and wartime supplies.',
            'Space Age Observatory': 'An observatory near Mars. Telescopes and futuristic equipment fill the '
                                     'room.',
            'Futuristic Laboratory': 'A high-tech laboratory with advanced machinery and prototypes.',
            'Victorian Era Parlor': 'A luxurious parlor from the Victorian era, adorned with elegant furniture and '
                                    'decor.',
            'Medieval Castle Dungeon': 'A dark and damp dungeon within a medieval castle. Rusty chains hang from the '
                                       'walls.',
            'Prehistoric Cave': 'A cave from the prehistoric era. The air is thick, and primitive drawings mark the '
                                'walls.'
        }

        self.player_inventory = []

    def display_room_description(self, room_name):
        print(f"\n{room_name}:\n{self.descriptions[room_name]}")

        # Use get method to handle KeyError
        item_in_room = self.items.get(room_name, None)
        if item_in_room is not None:
            print(f"Item in this room: {item_in_room}\n")
        else:
            print("No item in this room.\n")

    def replace_items_with_prison_cube(self):
        items_to_replace = ['Amulet of blood', 'Mask of Tutankhamun', 'Compass',
                            'Astronaut Gloves', 'Sonic Screwdriver', 'Tiara', 'Rusted Key']

        if all(item in self.player_inventory for item in items_to_replace):
            print("\nCongratulations! You have collected all required items.")
            print("Your items have evolved into the 'Prison Cube'.")
            self.player_inventory = ['Prison Cube']

    def check_win_condition(self, room_name):
        if 'Prison Cube' in self.player_inventory and room_name == 'Prehistoric Cave':
            print("\nCongratulations! You have successfully collected all items and saved the timeline.")
            print("You win! Thanks for playing.")
            sys.exit()

    def search_room_for_item(self, room_name):
        # Use get method to handle KeyError
        item_in_room = self.items.get(room_name, None)

        if item_in_room is not None:
            user_input = input(f"Do you want to search for the '{item_in_room}' in this room? (Y/N): ").upper()

            if user_input == 'Y':
                print(f"You found the '{item_in_room}'! Adding it to your inventory.")
                self.player_inventory.append(item_in_room)
                del self.items[room_name]
                self.check_all_items_collected()
                self.replace_items_with_prison_cube()
                self.check_win_condition(room_name)
        else:
            print("No item to search in this room.")

    def check_all_items_collected(self):
        # When all items are collected the player's inventory changed to one ultimate item
        if all(item == 'Prison Cube' for item in self.player_inventory):
            print("\nCongratulations! You have found all items, and they have evolved into the 'Prison Cube'.")

    def check_prison_cube_on_entering_cave(self):
        # if the ultimate item is not in inventory when player enters Prehistoric Cave, Loose!
        if 'Prehistoric Cave' in self.rooms and 'Prison Cube' not in self.player_inventory:
            print("\nYou enter the Prehistoric Cave, but you do not have the 'Prison Cube'. Game Over!")
            game_over()

    def play_game(self):
        # Main Gameplay
        room_name = 'Time Headquarters'
        display_room_with_border(room_name)  # Room Header
        self.display_room_description(room_name)  # Room Description
        self.search_room_for_item(room_name)  # Check if item in current room

        while True:
            directions = ', '.join(self.rooms[room_name].values())
            next_move = input(  # Get and print current room directions
                f"Available directions: {directions}\nEnter the direction you want to go, or type 'E' to exit: ")

            if next_move.upper() == 'E':
                print("Exiting the game. Goodbye!")
                break

            possible_destinations = [room for room, direction in self.rooms[room_name].items() if
                                     direction.upper() == next_move.upper()]
            if possible_destinations:
                next_destination = possible_destinations[0]
                move_through_portal(next_destination)
                room_name = next_destination
                self.display_room_description(room_name)
                self.search_room_for_item(room_name)
                self.replace_items_with_prison_cube()

                # Check for win condition
                self.check_win_condition(room_name)

                # Check for Prehistoric Cave condition
                if room_name == 'Prehistoric Cave':
                    self.check_prison_cube_on_entering_cave()

            else:
                print("Invalid move. You cannot go in that direction from here.")


# Initiate start room
start_room = START_ROOM
# Display Title and Story Background
intro = TitleIntro()  # Create an instance of the TitleIntro class
intro.display_welcome_text()  # Call the method to display welcome text

# Press ENTER to continue
if press_enter_to_continue():
    print()
else:
    print("Game is exiting...")

while True:
    hero_name = input("Enter your name.\n(Or the name of our hero.)")  # Gets hero's name from user
    # Check to see if input is characters only.
    if re.match("^[a-zA-Z]+$", hero_name):
        break
    else:
        print("\nInvalid input. Please enter characters only, without numbers or special characters.")
        print()

print()
...
# Rest of the code
print("""
            ! RING RING RING !
            You roll over to check your phone and see your boss calling.""")
print()
boss_message = f"""
            "{hero_name} there has been an emergency at the agency! I need you here as soon as possible, the fate of the
            world is in your hands! Do you still have your mobile teleporter?"
"""
answer_phone = input(str("To answer phone, press 'P'"))
if answer_phone.upper() == 'P':  # Some fun text if an invalid response is inputted by user
    print(boss_message)
else:
    print("""
            As much as you dont want to...
            **IT IS YOUR BOSS, YOU MUST ANSWER IT**
            You reach over and accept the call.
            """)
    print(f"{boss_message}")

boss_instructions = f"""
            "Thank goodness! Get to the {START_ROOM.lower()} and I will explain the situation."
            \n"""
answer_teleporter_question = input(str("Press 'Y' for Yes.\nPress 'N' for No."))
if answer_teleporter_question.upper() == 'Y':  # More fun text if invalid response
    print(boss_instructions)
else:
    print("""
            You begin to say that you left your teleporter at the agency headquarters but then you see it laying on 
            the counter next to your phone...
            "Yes sir, I have it here."
            """)
    print(f"{boss_instructions}")

print(f"""
            You hang up the phone and get into your black robe uniform.
            Using your teleporter you open a portal to the {START_ROOM.lower()}""")
print()

if press_enter_to_continue():  # Press Enter to continue
    print()
else:
    print("Game is exiting...")

# Move through a portal and display the new room header (Starting Room)
print(f"A PORTAL OPENS AND YOU ENTER THE PORTAL\nYou are now in the {START_ROOM})")
display_room_with_border(START_ROOM)

# Message from player's boss
print(f"""
            "{hero_name} A grave concern has arisen regarding the stability of the temporal continuum. Numerous minute 
            temporal rifts have manifested across time. While the current repercussions on the timeline remain within 
            manageable bounds, intelligence reports have identified the source of these anomalies. The instigator is 
            none other than the Chronos Saboteur, a former operative of The Keepers, who has deviated from their ranks. 
            It is strongly suspected that the saboteur is traversing the vast expanse of time and space with the 
            intention of manipulating pivotal events. Should these endeavors persist unchecked, the ensuing damage to 
            the timeline poses a severe threat, placing the entirety of existence in jeopardy."

            "Your designated mission entails the retrieval of specific artifacts possessing the capability to construct 
            a temporal prison, thereby restraining Chronos and mitigating this imminent peril. Regrettably, these vital 
            artifacts have been dispersed across different temporal epochs. Recognizing the inevitability of our 
            resorting to this countermeasure, Chronos preemptively purloined them from archival repositories. 
            Fortunately, our tracking mechanisms remain operational, and a comprehensive list of the artifacts will be
            furnished to facilitate your pursuit."


            -The list of locations have been imported into your teleporter. 

            "Good luck, {hero_name}. We are counting on you!"
""")
if press_enter_to_continue():  # Press Enter to continue
    print()
else:
    print("Game is exiting...")
# Start the journey // Call Main gameplay class
play_instance = StartJourney()
play_instance.play_game()
