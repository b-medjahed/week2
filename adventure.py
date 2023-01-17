print("\nWelcome to the Adventure Game!\n ")
print("\nIt takes place in a scary obscure cave.\n")
print("\nIn order to exit safely you have to consider the following options: forward, backward, left, right.\n ")
print("Beware there will times where you may hit a wall!!!\n")
global dead_end1
global pick_up_sword
global anti_venom



#Define functions
#Define entrance function which represents the starting point when entering the cave.
#User can only go forward or right.
def entrance():
    print("\nAdventurer, you have entered a very dangerous cave! You can leave with Gold or...\n")
    option=""
    options=["forward", "right"]
    while option not in options:
        option=input("You can either go forward or right! Make up your mind: ")
        if option=="forward":
           skeleton()
        if option=="right":
           sword()
        else:
            print("\nType in the correct option.\n")

def sword():
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
           skeleton()
        if option=="right":
           wall1()
        if option=="forward":
           anti_venom()
        else:
            print("\nType in the correct option.\n")

def wall1():
    print("\nYou have hit a wall. You must go backward!\n")  
    dead_end1=True
    sword()

def AntiVenom(): 
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


