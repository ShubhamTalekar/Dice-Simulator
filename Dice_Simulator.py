import random
import time


def dice_roll():
    r = (random.randint(1, 6))
    time.sleep(1)
    print("rolling...")
    time.sleep(1)
    print("rolling...")
    time.sleep(1)
    int(r)
    return r


Players = list()


def player_s():
    print("Enter the number of players:")
    player = input("")

    if player == "1":
        p1 = input("Enter Player 1:")
        print("Successfully Added " + p1 + "!")
        Players.append(p1)

    elif player == "2":
        p1 = input("Enter Player 1:")
        print("Successfully Added " + p1 + "!")
        Players.append(p1)
        time.sleep(2)
        p2 = input("Enter Player 2:")
        print("Successfully Added " + p2 + "!")
        Players.append(p2)

    elif player == "3":
        p1 = input("Enter Player 1:")
        print("Successfully Added " + p1 + "!")
        Players.append(p1)
        time.sleep(2)
        p2 = input("Enter Player 2:")
        print("Successfully Added " + p2 + "!")
        Players.append(p2)
        time.sleep(2)
        p3 = input("Enter Player 3:")
        print("Successfully Added " + p3 + "!")
        Players.append(p3)

    elif player == "4":
        p1 = input("Enter Player 1:")
        print("Successfully Added " + p1 + "!")
        Players.append(p1)
        time.sleep(2)
        p2 = input("Enter Player 2:")
        print("Successfully Added " + p2 + "!")
        Players.append(p2)
        time.sleep(2)
        p3 = input("Enter Player 3:")
        print("Successfully Added " + p3 + "!")
        Players.append(p3)
        time.sleep(2)
        p4 = input("Enter Player 4:")
        print("Successfully Added " + p4 + "!")
        Players.append(p4)
    else:
        print("Enter a Valid Number!")
        return player_s()


player_s()

print(" ")
print("The Players are:")
time.sleep(2)
for x in Players:
    print(x)
    time.sleep(1)
print(" ")
time.sleep(1)
print("Welcome To Dice Simulator")
time.sleep(1)
print("[]")
time.sleep(1)
print("Start")
print(" ")
time.sleep(1)


def player_die():
    user = input("Roll Dice?(if yes press Enter)")
    if user == "":
        kg = 1
        while kg == 1:
            for i in range(0, len(Players)):
                time.sleep(3)
                print(Players[i])
                dice_op = dice_roll()
                print(dice_op)
                print(" ")
                while dice_op == 6:
                    time.sleep(1)
                    print("Another Turn")
                    dice_op = dice_roll()
                    print(dice_op)
                    print(" ")
            kg = int(input("Keep Rolling?(1/0): "))
            if kg == 0:
                print("Thank you for playing")
            elif kg == 200599:
                time.sleep(1)
                print("Project")
                time.sleep(1)
                print("by")
                time.sleep(1)
                print("Shubham Talekar")
    else:
        print("you haven't pressed enter")
        return


player_die()
