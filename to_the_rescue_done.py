# Import all necessary libraries
import sys
import time
import random
from tkinter import Y


# Function to Colour the text
def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"

# Function for Typewriting Printing
# (Printing strings one charcter at a time)
def sg_print(string):
    string=colored(0,255,0,string)
    for word in string:
       sys.stdout.write(word)
       sys.stdout.flush()
       time.sleep(0.0001)
# it's the slow print in red
def sr_print(string):
    string=colored(255,0,0,string)
    for word in string:
       sys.stdout.write(word)
       sys.stdout.flush()
       time.sleep(0.0001)

###############################
# Function for GAME OVER screen
###############################

def game_over():
  print(colored(255,0,0,r"""
░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
  ░█████╗░██╗░░░██╗███████╗██████╗░
  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""))        
  play_again()


#################################
# Function for playing again
#################################

def play_again():
  sr_print("\nEnter 'y' to Play Again  or 'n' to exit the game.")
  a = input("> ")
  if a.lower() == "y":
    intro()
  elif a.lower() == "n":
    exit()
  else:
      play_again()
#################################
# Function for Character Creation
#################################

def partner():
  while 1:
    sg_print("Excellent! What shall I call you?")
    ans = input("> ")
    y=set("1234567890&*()_/\$\"'%^&*()!?|")
    if any((i in y) for i in ans):
      sr_print("Please enter your name correctly!\n")
     
    
    elif len(ans) <3 :
      sr_print("You're name needs to be more than 2 character!\n")
      
    
    else:
      sg_print(f"Welcome to the team {ans}.")
      break

###########################################
# Function for the Introduction to the game
###########################################

def intro():
    global key_collected
    key_collected = False
    print(colored(0,255,255,"""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

    ████████╗██╗░░██╗███████╗  ██████╗░███████╗░██████╗░█████╗░██╗░░░██╗███████╗
    ╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝
    ░░░██║░░░███████║█████╗░░  ██████╔╝█████╗░░╚█████╗░██║░░╚═╝██║░░░██║█████╗░░
    ░░░██║░░░██╔══██║██╔══╝░░  ██╔══██╗██╔══╝░░░╚═══██╗██║░░██╗██║░░░██║██╔══╝░░
    ░░░██║░░░██║░░██║███████╗  ██║░░██║███████╗██████╔╝╚█████╔╝╚██████╔╝███████╗
    ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░░╚═════╝░╚══════╝
""")) 
    time.sleep(2)
    sg_print("Welcome to the game!\nMy name is Sherlock and I need your help in searching for the missing person!")

    print(colored(0,255,255,r"""

                             /^\/^\
                             \----|
                         _---'---~~~~-_
                          ~~~|~~L~|~~~~
                             (/_  /~~--
                           \~ \  /  /~
                         __~\  ~ /   ~~----,
                         \    | |       /  \
                         /|   |/       |    |
                         | | | o  o     /~   |
                       _-~_  |        ||  \  /
                      (// )) | o  o    \\---'
                      //_- |  |          \
                     //   |____|\______\__\
                     ~      |   / |    |
                             |_ /   \ _|
                           /~___|  /____\            
"""))
    sg_print("""Would you like to help me to rescue the missing person?
Enter 'y' for YES or 'n' for NO""")
    while True:
        ans = input("> ")
        if ans.lower() == "y":
            partner()
            event1()
        elif ans.lower() == "n":
            sr_print("What a shame!\nWe would have made a good team!")
            game_over()
        else:
           sr_print("Please enter 'y' or 'n'")

######################
# Function for Event 1
######################

def event1():
  sg_print("\n\nLet's get started!")
  print(colored(0,255,255,r"""

              ,;;;,
             ;;;;;;;
          .-'`\, '/_
        .'   \ ("`(_)
       / `-,.'\ \_/
       \  \/\  `--`
        \  \ \
         / /| |
        /_/ |_|
      ( _\ ( _\  #:##        #:##        #:##         #:##
                        #:##        #:##        #:##
"""))
  sg_print("""You are on your way to find the victim,
you encounter two ways - one of them leads you to an abandoned building
and other leads you a jungle!""")
  sg_print("""
Which way would you like to go? 
Enter '1' for the Abandoned Building
Enter '2' for the Jungle
""")
  while True:
    answer = input("> ")
    if answer == "1":
      print(colored(0,255,255,r"""
                                               /\      /\
                                               ||______||
                                               || ^  ^ ||
                                               \| |  | |/
                                                |______|
              __                                |  __  |
             /  \       ________________________|_/  \_|__
            / ^^ \     /=========================/ ^^ \===|
           /  []  \   /=========================/  []  \==|
          /________\ /=========================/________\=|
       *  |        |/==========================|        |=|
      *** | ^^  ^^ |---------------------------| ^^  ^^ |--
     *****| []  [] |           _____           | []  [] | |
    *******        |          /_____\          |      * | |
   *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| |
  ***********]  [] |  []  []  |  |  |  []  []  | ===***** |
 *************     |         @|__|__|@         |/ |*******|
***************   ***********--=====--**********| *********
***************___*********** |=====| **********|***********
 *************     ********* /=======\ ******** | *********
"""))
      time.sleep(1)
      sg_print("now you are in the abandon building")
      print(colored(0,255,255,r"""
      ###, ,##, ,##,
       #  # #  # #  #
       ###  #  # #  #
       #  # #  # #  #
       ###' '##' '##'
            .--,
           /  (
          /    \
         /      \ 
        /  0  0  \
((()   |    ()    |   ()))
\  ()  (  .____.  )  ()  /
 |` \_/ \  `""`  / \_/ `|
 |       `.'--'.`       |
  \        `""`        /
   \                  /
    `.              .'    ,
    |`             |  _.'|
     |              `-'  /
     \                 .'
      `.____________.-'
"""))
      time.sleep(2)
      sr_print ('You have been horror-struck and killed by a ghost\n\n!')
      game_over()
      break
    elif answer == "2":
      sg_print("you are in the jungle way")
      print(colored(0,255,255,r"""

               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
"""))

      # Event 1 has been PASSED. Progress to Event 2
      event2()
      break
    else:
      print("Please enter '1' or '2'")   

######################
# Function for Event 2
######################


def event2():
    # Randomise the lock combination during each playthrough
    lock_com = str(random.randint(1000,9999))
    # Function for opening the strongbox
    def crack_the_code():
        global key_collected
        code = input("Enter the code\n> ")
        
        if code == lock_com:
            sg_print("\nYou enter the code and the lock pops open!\nInside the strongbox you find a car key.")
            
            key_collected = True
            print(colored(255, 0, 0, r"""

   CAR KEY ACQUIRED!!
     _____________
    /      _      \
    [] :: (_) :: []
    [] ::::::::: []
    [] :: CAR :: []
    [] :: KEY :: []
    [] ::::::::: []
    [_____________]
        I     I
        I_   _I
         /   \
         \   /
         (   ) 
         /   \
         \___/"""))

        else:
            sg_print("You enter the code but nothing happens\nDo you want to try again?\nEnter 'Y' for Yes or 'N' for NO")
            try_again = input ("> ")
            if try_again.lower() == "y":
                # rerun the function to try again
                crack_the_code()
                # else leave the function
    
    # Introduction to new area

    sg_print("""
You arrive at the camp within the jungle but to your suprise, you find it abandoned. 
You look around the camp, there's not much left but you can see an small cage, 
overturned table & chairs, the remains of a fire, 
and a lone Jeep next to sets of tyre tracks leading away from the camp.
It is clear that whoever was last here had left in a hurry.
""")

    # INSERT GRAPHICS OF THE CAMP

    # Collecting Evidence
    
    map_found = False
    searched_1 = False
    searched_2 = False
    searched_3 = False

    i = 1
    while i > 0:
    
        #Check if user has already searched
        if i > 1:
            i = 2
            sg_print("\nWhere would you like to search next?\n")
        
        print(colored(0, 255, 0, """
Enter '1' to investigate the Cage
Enter '2' to investigate the Table & Chairs
Enter '3' to investigate the Fire
Enter '4' to investigate the Tyre Tracks"""))
        if i > 1:
            print(colored(0, 255, 0, "Enter '5' if you are ready to leave"))

        searching = input("\n> ")
        # AREA 1
        if searching == "1":
            if searched_1 == False:
                sg_print("""
You head over to investigate the cage.
As you look inside, something in the mud catches your eye
it's *SENTIMENTAL ITEM*. This proves it! *MISSING PERSON* was definitely here
""")
                searched_1 = True
            else:
                sg_print("""You go back and search the cage again but find nothing new.""")

            # Return item to missing person at the end
            # The prisoner doesn't seem to be here any more
            # INSERT GRAPHICS
            i += 1
        # AREA 2
        elif searching == "2":
            if searched_2 == False and key_collected == False:
                sg_print("""
You head over to investigate the table & chairs.

""")
                searched_2 = True
                crack_the_code()
            # You find a lockbox with a combination lock
            elif searched_2 == True and key_collected == False:
                sg_print("You return to the strongbox to try again")
                crack_the_code()
            else:
                sg_print("You go back and search the overturned table & chairs again but find nothing new.")
            i += 1
        # AREA 3
        elif searching == "3":
            if searched_3 == False:
                sg_print(f"""
You head over to investigate the fire.
You bend down and wave your hand over the ash,
there is still a gentle heat radiating from it.
Whoever was here left not long ago,
if you hurry you can still catch them!
Beside the ashes you find a burnt scrap of paper, 
there is not much left on it but you can make out the number {lock_com}
""")
                searched_3 = True
            else:
                sg_print("You go back and search around the fire again but find nothing new.")
            i += 1
        # AREA 4
        elif searching == "4":            
            if map_found == False:
                sg_print("""
You head over to investigate the Jeep and tyre tracks. 
As you walk around the Jeep you spot something
It's a map of the jungle!
You can see that someone has drawn a route on the map
that leads away from the camp and towards a new location.
That must be where they've taken *MISSING PERSON*!
""")
                # INSERT GRAPHICS OF MAP
                map_found = True
            elif map_found == True:
                sg_print("You go back search the tyre tracks again but find nothing new")
            i += 1
        # AREA 5 / LEAVE
        elif i > 1 and searching == "5":
            sg_print("\nAre you sure you're ready to leave?\nEnter 'Y' for YES or 'N' for NO")
            while True:
              cont = input("\n> ")
              if cont.lower() == "y":
                if key_collected == True and map_found == True:
                    sg_print("\nYou steal the Jeep and following your map, head further into the jungle...")
                    return event3()
                elif key_collected == True and map_found == False:
                    sr_print("""
You steal the Jeep and head into the jungle but without knowing where to go
you get lost and take a wrong turn off a cliff, plummeting to your death.
""")
                    game_over()
                    # break
                elif key_collected == False and map_found == True:
                    sr_print("""
You head into the jungle on foot, following the map
but you encounter a wild jaguar, with no way to defend yourself you attempt to run away
but you are unable to escape the jaws of it
""")
                    game_over()
                    # break
                elif key_collected == False and map_found == False:
                    sr_print("""
You head into the jungle on foot and wander aimlessly, 
hoping you are somehow
""")
                    game_over()
                    # break
              elif cont.lower() =="n":
                sg_print("You return the to camp and continue looking for clues")
                break
              else:
                 sr_print("\nAre you sure you're ready to leave?\nEnter 'Y' for YES or 'N' for NO")         
        else:
            sr_print("\nINVALID INPUT!\nPlease enter a valid input\n")

#########################
# Function for Event 3
#########################

def event3():

  axe_collected = False

  # Find Axe
  sg_print("""
You make it most of the way through the jungle but a tree has fallen in the road
You are unable to move the tree or drive around it.
With the clock against you, you decide you must leave the Jeep and make the final leg of the journey on foot""")
  sg_print("Whilst walking through the jungle, you stumble across an axe buried in the ground")
  print(colored(0,0,255,r"""
  _________________.---.______
 (_(______________(_o o_(____()
              .___.'. .'.___.
              \ o    Y    o /
               \ \__   __/ /
                '.__'-'__.'
                    '''
  """))
  sg_print("Would you like to pick up the axe?\nEnter 'y' for YES\nEnter 'n' for NO")
  while True:
   ans = input("\n> ")
   ans.lower()
   if ans.lower() == "y":
    sg_print("Why not, you now have the axe.")
    print(colored(0,0,255,r"""

         .----.      __) `\
         | == |     < __=- |
      ___| :: |___   \\ `)/
      \  `----'  /\  (\) (
       \   `.   /( \/ /\\
       |    :   | \  /  \\
       \   _._  /  `"   <_>
        xxx(o)xx
"""))
    axe_collected = True
    break
   elif ans.lower() == "n":
    sr_print("No! I have no need for an axe.\n")
    break
   else:
    sr_print("Would you like to pick up the axe?\nEnter 'y' for YES\nEnter 'n' for NO")
  # Python Encounter (With Axe)
  sr_print("""As you continue through the jungle, 
you are startled by the sound of hissing 
as a giant python slithers out from the grass and blocks your path
""")
  if axe_collected == True:
    
    print(colored(0,0,255,r"""

              /^\/^\
            _|__|  O|
    \/     /~     \_/ \
    \____|__________/  \
          \_______      \
                  `\     \                 \
                    |     |                  \
                  /      /                    \
                  /     /                       \\
                /      /                         \ \
              /     /                            \  \
            /     /             _----_            \   \
            /     /           _-~      ~-_         |   |
          (      (        _-~    _--_    ~-_     _/   |
            \      ~-____-~    _-~    ~-_    ~-_-~    /
              ~-_           _-~          ~-_       _-~
                ~--______-~                ~-___-~

                 /\_[]_/\
                |] _||_ [|
         ___     \/ || \/
        /___\       ||
       (|0 0|)      ||
     __/{\U/}\_ ___/vvv
    / \  {~}   / _|_P|
    | /\  ~   /_/   []
    |_| (____)        
    \_]/______\        
       _\_||_/_           
      (_,_||_,_) 
"""))
    sr_print("""The python is hungry and strikes at you!
Would you like to fight the python?
Enter 'y' for YES
Enter 'n' for NO
""")
    while True:
     ans = input("> ")
     if ans.lower() == "y":
      sg_print("You have slain the python with your axe and continue with your investigation")
      return event4()
     elif ans.lower() == "n":
      sr_print("You have been killed by the python")
      game_over()
     else:
          sr_print("""Would you like to fight the python?
Enter 'y' for YES
Enter 'n' for NO""")
  # Python Encounter (Without Axe)
  else:
    print(colored(0,0,255,r"""

             /^\/^\
           _|__|  O|
  \/     /~     \_/ \
  \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~ 

                                        /___\                                                 
                                       (|0 0|)                                                    
                                     __/{\U/}\_ ___                                                
                                    / \  {~}   / _|                                                 
                                    | /\  ~ /_/| /                                                   
                                    |_| (____) |_|                        
                                   \_] /______\ \_]
                                        _\_||_/_             
                                       (_,_||_,_)"""))
    sr_print("""The python is hungry and strikes at you!
Would you like to fight the python?
Enter 'y' for YES
Enter 'n' for NO
""") 
    while True:
      ans = input("> ")
      if ans.lower() == "y":
       sr_print("""Unfortunetly you didn't pick up the axe,
       the pyhton wraps itself around your neck, makes it hard for you to breathe,
it suffocates you, til you cant breathe. You have died!
""")
       game_over()
      elif ans.lower() == "n":
        sr_print("You have been killed by the python!")
        game_over()
      else:
        sr_print("""Would you like to fight the python?
Enter 'y' for YES
Enter 'n' for NO
        """)




def event4():
    sg_print("\nNow that the python is dealt with you continue walking, from your view you can see a fire, you see a group of people sat around the fire, and a hut which is un-guarded. You approach the hut")
    print(colored(255,255,0,r""" 
                    _.--._
                _.-'(//|(\'-._
            _.-'(\)))(\\\\((|\'-._
        _.-')/)/)\((|\))/(/\()\\(/'-._
     .-'/))/))(\\))\)//)\\)))(/))\)(\\'-.
    /')/)\(/\)\))/\(/|)\))/((||\/)\)\)\\'\
    \((\\(/((\///)))/(\\(/)\\\\\)\)\))\))/
     V )/.-.__(/|_/|' ' ' |\_|)/__.-. ))V
       | |    | |_/| ' ' '|\_| |    | |
       | |    | |_/|' '  '|\_| |    | |
       | '-.__| |_/| ' ' '|\_| |__.-' |
       |        |_/|'  ' '|\_|        |
       |_       |_/| ' ' '|\_|       _|
       ||'-._   |_/|______|\_|   _.-'||
       ||    '-.|_/<      >\_|.-'    ||
       ||      ||\__________/||      ||
       ||      || \________/ ||      ||
       ||      ||  \______/  ||      ||
       ||      ||  |______|  ||      ||
               ||  |______|  ||
               ||  |______|  ||
"""))
    sg_print("""
The person is trapped in a controlled room, you try open the door but are unable to.
You need to answer the riddle correctly to open the door, 
if you fail 3 times gas will fill the room and the missing person will die

The alphabet goes from A to Z but i go Z to A.""")
    attempt = 3
    while attempt > 0:
        sg_print("\nWhat am I?")
        ans = input ("\n> ").lower()
        if "zebra" in ans:
          sg_print("You have solved the riddle, the door is opened, you have rescued the missing person safely")
          print(colored(0,255,255,r"""
                                                                                                           
 _|          _|  _|_|_|_|  _|        _|                _|_|_|      _|_|    _|      _|  _|_|_|_|  
 _|          _|  _|        _|        _|                _|    _|  _|    _|  _|_|    _|  _|        
 _|    _|    _|  _|_|_|    _|        _|                _|    _|  _|    _|  _|  _|  _|  _|_|_|    
   _|  _|  _|    _|        _|        _|                _|    _|  _|    _|  _|    _|_|  _|        
     _|  _|      _|_|_|_|  _|_|_|_|  _|_|_|_|          _|_|_|      _|_|    _|      _|  _|_|_|_|  
"""))
          
          return play_again()
        else: 
          attempt -=1
        sr_print(f"{ans} is not the right answer please Try Again, you have {attempt} more attempt!")
    
    if attempt == 0:
        game_over()


#Here I run the code        
intro()