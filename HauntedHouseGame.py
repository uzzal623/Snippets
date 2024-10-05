#Haunted House Game

import random

class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = []

class Player:
    def __init__(self):
        self.inventory = []

def create_rooms():
    return {
        "Entrance": Room("Entrance", "You're at the entrance of a creepy old house.", {"north": "Living Room"}),
        "Living Room": Room("Living Room", "A dusty living room with cobweb-covered furniture.", {"north": "Kitchen", "east": "Library", "south": "Entrance"}),
        "Kitchen": Room("Kitchen", "A dark kitchen with rusty utensils.", {"south": "Living Room", "east": "Dining Room"}),
        "Library": Room("Library", "Rows of old books line the walls.", {"west": "Living Room", "north": "Dining Room"}),
        "Dining Room": Room("Dining Room", "A grand dining table with moldy plates.", {"west": "Kitchen", "south": "Library", "north": "Exit"}),
        "Exit": Room("Exit", "You've found the exit!", {})
    }

def add_items(rooms):
    rooms["Living Room"].items.append("Key")
    rooms["Kitchen"].items.append("Flashlight")
    rooms["Library"].items.append("Book")
    rooms["Dining Room"].items.append("Candle")

def display_room(room):
    print(f"\n--- {room.name} ---")
    print(room.description)
    if room.items:
        print(f"You see: {', '.join(room.items)}")
    print(f"Exits: {', '.join(room.exits.keys())}")

def get_player_choice(room, player):
    while True:
        choice = input("\nWhat would you like to do? ").lower().split()
        if not choice:
            print("Please enter a command.")
            continue

        action = choice[0]
        if action in ["go", "move"]:
            if len(choice) < 2:
                print("Go where?")
                continue
            direction = choice[1]
            if direction in room.exits:
                return ("move", direction)
            else:
                print(f"You can't go {direction}.")
        elif action in ["take", "grab", "pick"]:
            if len(choice) < 2:
                print("Take what?")
                continue
            item = " ".join(choice[1:])
            if item in room.items:
                return ("take", item)
            else:
                print(f"There's no {item} here.")
        elif action == "inventory":
            if player.inventory:
                print(f"You are carrying: {', '.join(player.inventory)}")
            else:
                print("Your inventory is empty.")
        elif action in ["quit", "exit"]:
            return ("quit", None)
        else:
            print("I don't understand that command.")

def main():
    rooms = create_rooms()
    add_items(rooms)
    player = Player()
    current_room = rooms["Entrance"]
    moves = 0

    print("Welcome to Haunted House Escape!")
    print("Navigate through the house and find the exit.")
    print("Commands: 'go [direction]', 'take [item]', 'inventory', 'quit'")

    while current_room.name != "Exit":
        display_room(current_room)
        action, target = get_player_choice(current_room, player)

        if action == "move":
            current_room = rooms[current_room.exits[target]]
            moves += 1
        elif action == "take":
            player.inventory.append(target)
            current_room.items.remove(target)
            print(f"You picked up the {target}.")
        elif action == "quit":
            print("Thanks for playing!")
            return

        if moves == 15:
            print("\nA ghost appears and scares you away! Game Over.")
            return

    print("\nCongratulations! You've escaped the haunted house!")
    print(f"You escaped in {moves} moves and collected {len(player.inventory)} items.")

if __name__ == "__main__":
    main()
