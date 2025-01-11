import ascii
ascii.printing()
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
des1 = input("You are in a mine and there are two tunnels(right and left).What direction do you go in.\n")
if des1.lower() == "left":
    des2 = input("You get out of the cave but now you are stranded\n"
                 "on the neighbor island of the island with the treasure.\n"
                 "Do you swim to the other island or do you wait.\n")
    if des2.lower() == "wait":
        des3 = input("When it gets dark outside you see a campfire and you go there.From there you see a house\n"
                     "with a note that says 'Dear pirate, you have found the treasure.\n"
                     "It is in one of the three entrances.'You see a red door, a blue door,and a yellow door.\n"
                     "Which door do you chose.\n")
        if des3.lower() == "yellow":
            print("Congratulations! You win!")
        elif des3.lower() == "red":
            print("In there is an old tribe. They attack you with their spears.\nGame over.")
        else:
            print("You see a lion. It attacks you.\nGame over.")
    else:
        print("You were eaten by a big shark.\nGame over.")
else:
    print("You fall into a deer trap.\nGame over.")