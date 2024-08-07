print("Welcome to treasure Island")
print("Your mission is to find the treasure")
print("You're at the cross road. Where do you want to go?")
left_or_right = input('Type "left" or "right" ')
if left_or_right == "left":
    print("You've come to a lake. There is an Island in the middle of the lake.")
    boat_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across" ')
    if boat_or_swim == "wait":
        print("You arrive at the island  unharmed. There is a house with 3 doors. One red, One yellow and One blue.Which color will you choose?")
        door_color = input('Choose "red", "yellow" or "blue" ')
        if door_color == "red":
            print("It's a room full of fire. Game Over")
        elif door_color == "yellow":
            print("You found the treasure. You win!")
        elif door_color == "blue":
            print("You enter a room of beasts. Game Over")
        else:
            print("Choose the proper color.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into  hold. Game Over")
        