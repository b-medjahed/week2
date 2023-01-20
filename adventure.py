
#Define functions
#Define entrance function which represents the starting point when entering the cave.
#Each function defines: a room, a wall or an exit.
#User can go forward, right or left.
#User will automatically go backward if they hit a wall.


def entrance():
    print("\nAdventurer, you have entered a very dangerous cave! You can leave with Gold or...\n")
    option=""
    options=["forward", "right"]
    while option not in options:
        option=input("You can either go forward or right! Think carefully!: ")
        if option=="forward":
           remains()
        if option=="right":
           sword()
        else:
            print("\nType in the correct option.\n")


def sword():
    global pick_up_sword
    pick_up_sword=True
    option=""
    options=["forward", "right","left"]
    if dead_end1==True:
       print("\nAdventurer, welcome to the sword-room Again. Remember not to go right!\n") 
    else:
       print("\nAdventurer, welcome to the sword-room! Pick up the sword and get ready...\n")
    while option not in options:
        
        option=input("You can either go forward, left or right! Make up your mind: ")
        if option=="left":
           remains()
        if option=="right":
           wall1()
        if option=="forward":
           AntiVenom()
        else:
            print("\nType in the correct option.\n")

def wall1():
    global dead_end1
    print("\nYou have hit a wall. You must go backward!\n")  
    dead_end1=True
    sword()



def remains():
    option=""
    options=["forward", "right"]
    print("\nAdventurer, you can see animal remains. Adventurer hears a disturbing hissing sound ahead.!\n") 
    while option not in options:
        
        option=input("You can either go forward or right! Your decision defines your destiny: ")
        if option=="forward":
           snake()
        if option=="right":
           AntiVenom()
        else:
            print("\nType in the correct option.\n")


def snake():
    global anti_venom
    global pick_up_sword
    
    print("\nAdventurer, you can see a venomous snake!\n") 
    option=""
    options=["fight", "escape"]
    while option not in options:
        fight=input("\nYou can fight or escape. Type in fight OR escape: ")
        if fight=='fight':
            if anti_venom==True and pick_up_sword==True:
               print("\nYou have defeated the snake.\n" )
               exit1()
            else:
               print("\nYou can only defeat this  venomous snake if you have a sword and antidote!\n")
               print("\nYou have lost this fight!\n")
               print("\nGAME OVER\n")
               quit()
        if fight=='escape':    
             remains()
        else:
             print("\nType in the correct option.\n")

def trail():
    option=""
    options=["forward", "right", "left"]
    print("\nAdventurer, the end is near or is it... \n")
    print("\nAdventurer notices trail of golds \n")
    while option not in options:
        option=input("You can either go forward, left or right! Make up your mind: ")
        if option=="left":
           snake()
        if option=="right":
           exit2()
        if option=="forward":
           wall2()
        else:
            print("\nType in the correct option.\n")

def wall2():
     global dead_end2
     print("\nYou have hit a wall. You must go backward!\n")
     dead_end2=True
     trail()

def exit2():
        print("\nCongratulations adventurer! You have made it out of the spooky cave\n")
        print("\nHere is a chest of gold for making it out alive\n")
        print("\nGAME COMPLETED\n")
        quit()

def exit1():
        print("\nCongratulations adventurer! You have made it out of the spooky cave\n")
        print("\nHere is a chest of gold for making it out alive\n")
        print("\nGAME COMPLETED\n")
        quit()

def villain():
    global pick_up_sword
    option=""
    options=["fight", "escape"]
    print("\nAdventurer, you have met the axe wielding villain!\n")
    fight=""
    while fight not in options:
         fight=input("\nYou can fight or escape. Type in fight OR escape: ")
         if fight=='fight':
            
            if pick_up_sword==True:
               while option not in options:
                    print("\nVillain challenged and defeated...\n")
                    exit2()
            else:
                print("\nVillain slices advnturer with the sharp axe!\n")
                print("\nGAME OVER\n")
                quit()
         if fight=='escape':    
             AntiVenom()
         else:
             print("\nType in the correct option.\n")

def AntiVenom(): 
    global anti_venom
    anti_venom=True
    option=""
    options=["forward", "right","left"]
    print("\nAdventurer, welcome to the antidote room!\n") 
    print("\nAdventurer, pick up the antidote! Beware what might come ahead...\n")
    while option not in options:
        
        option=input("You can either go forward, left or right! Make up your mind: ")
        if option=="left":
           snake()
        if option=="right":
           villain()
        if option=="forward":
           trail()
        else:
            print("\nType in the correct option.\n")
print("\nWelcome to the Adventure Game!\n ")
print("\nIt takes place in a scary cave.\n")
print("\nIn order to exit safely you have to consider the following options: forward, backward, left, right.\n ")
print("\nBeware there will be times where you may hit a wall!!!\n")

global dead_end1
global dead_end2
global pick_up_sword
global anti_venom

dead_end1=False
dead_end2=False
pick_up_sword=False
anti_venom=False
entrance()
        