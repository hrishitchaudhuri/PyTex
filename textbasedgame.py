# Initialize start locations.
x=0
y=0
chk=0

# Stores clues found within the game.
inventory=[]

# Initialize room variables.
inRoom = True
enterRoom = False

# Initialize timer.
import time
end=time.time()+300

# Print start message.
print("You are in the center of a room measuring 30 units by 20 units.")
print("Your task is to find all four keys scattered around this room.")
print("You are provided with a timer to tell you how long you have to escape, and a meter to check how close you are to a key.")
print("Your current coordinates will also be displayed to help guide you around the room.")
print()
print("Use the WASD keys to move around the room.")


# Initialize clue locations.
item_clu=[(-4,-6),(3,-4),(2,7),(-5,9)]

# Initialize active clue in map.
obj=item_clu[0]

# Define compass. 
def compass(a1,a2):
    """This function takes in the player and the clue's currrent position and guides them toward the nearest clue."""
    
    # Initialize player and clue locations locally
    x,x2 = a1[0],a2[0]
    y,y2 = a1[1],a2[1]

    if (x2-x)>0 and (y2-y)>0:
        print("Go North and East")   

    elif (x2-x)<0 and (y2-y)>0:
        print("Go North and West")
        
    elif (x2-x)>0 and (y2-y)<0:
        print("Go South and East")

    elif (x2-x)<0 and (y2-y)<0:
        print("Go South and West")

    elif (x2-x)==0 and (y2-y)>0:
        print("Go North")    

    elif (x2-x)==0 and (y2-y)<0:
        print("Go South")

    elif (x2-x)>0 and (y2-y)==0:
        print("Go East")

    elif (x2-x)<0 and (y2-y)==0:
        print("Go West")

    else:
        print("You have reached the destination")


# Define hot-cold meter.
def hotcold(a1,a2):
    """This function takes in the player and the clue's current locations and tells the player 
    if they're hot or cold with respect to the clue."""
    
    # Initialize player and clue locations locally.
    x,x2=a1[0],a2[0]
    y,y2=a1[1],a2[1]

    # Generate distance between player and clue.
    rad = ((x2-x)**2 + (y2-y)**2)**0.5

    if rad<37 and rad>18:
        print("COLD")

    elif rad<=18 and rad>7:
        print("WARM")

    else:
        print("HOT")


# Define hangman game.
def hangman():
    """This function simulates the hangman game. A word is chosen as the secret word and the player
    must guess it in order to end the game. The clues found will be autofilled into the word. As the player
    guesses, if the guess is correct, the letters will fill up in the word. Else, the player will lose a
    life."""
    
    # Initialize secret word. 
    word = "TREASURE"
    
    # Process and extract clues from inventory.
    global inventory
    charlist = list(map(lambda s: s[-2].lower(),inventory))

    # Initialize number of turns.
    turns = 3

    while turns > 0:  
        
        # Prompt user to guess.
        guess = input("Enter guess: ").lower()

        # If guess is correct, add letter to displayable characters.
        if guess in word.lower():
            charlist.append(guess)

        # Else, deduct a life. 
        if guess not in word.lower():
            print("Wrong")
            turns-=1
            print("You have", turns, 'more guesses') 


        # Initialize answer checking variable.
        failed = 0             
        
        # Print guessed answer fragment.
        for char in word:      
            if char.lower() in charlist:    
                print (char,end="")
            else:
                print ("_",end="")
                failed += 1    

        # Prepare win condition.
        if failed == 0:        
            print("\n","\n","Well done! You have won the game!",sep="")  
            global inRoom
            inRoom=False
            break
            
    # Prepare loss condition.
    if turns == 0:           
        print ("\n","\n","You have failed this game.",sep="")
        inRoom=False



# Prepare motion within room.
while inRoom:
        
        # Prepare timer end condition.
        if time.time()>=end:
                        print("Sorry you have failed this task.")
                        inRoom=False
                        break
        
        # Print timer.
        print("You have", round(end-time.time()),"seconds remaining")

        # Initialize movement input. Standard WASD movement.
        a=input().lower()
        if a == 'w':
            y += 1
            if y >= 10: 
                y =10
            print(x,y)
                
        elif a == 's':
            y += -1
            if y <= -10: 
                y = -10
            print(x,y)

        elif a =='d':
            x += 1
            if x >= 15: 
                x = 15
            print(x,y)
            
        elif a == 'a':
            x += -1
            if x <= -15: 
                x = -15
            print(x,y)

        elif a == 'exit':
            inRoom = False
            break

        elif a=='q':
            print(inventory)
            
        elif a=='stop':
            hangman()

        else: print('Movement restricted')

        # Print compass.
        compass((x,y),obj)

        # Print hot-cold value. 
        hotcold((x,y),obj)


        # Doors are at (3,-15).
        
        # Initialize walls.
        if x == -15 or x == 15:
            print('No further movement allowed further along the x-axis. You have encountered a wall.')
        
        if y == 10 or y == -10:
            print('No further movement allowed further along the y-axis. You have encountered a wall.')


        # Prepare clues.   
        if (x,y)==item_clu[0] and chk==0:
            print("Well done, you have found your first key."
            chk+=1
            inventory.append("key 1 - 'R'")
            print("Press Q to open your inventory and check your keys")
            obj=item_clu[1]

        if (x,y)==item_clu[1] and chk==1:
            print("Well done. You have found your second key.")
            chk+=1
            inventory.append("key 2 - 'T'")
            obj=item_clu[2]

        if (x,y)==item_clu[2] and chk==2:
            print("Well done. You have found your third key.")
            chk+=1
            inventory.append("key 3 - 'A'")
            obj=item_clu[3]
            
        if (x,y)==item_clu[3] and chk==3:
            print("Well done. You have found all four keys. Make your way to the exit now.")
            chk+=1
            inventory.append("key 4 - 'S'")
            obj=(-15,3)

        # End game.
        if (x,y)==(-15,3) and chk==4:
            hangman()
