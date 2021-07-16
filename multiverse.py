# import os
title = "Multiverse Maelstrom"
def start():
    print(f"""
                                   Hello traveler, Welcome to the {title}
    

                                   many adventures await you... Are you ready? 
    It has been a difficult time for people of Earth, and all the inhabitants of the Coffee Way...
    in a time in which philosophers were speculating on the ultimate meaning of life, the universe and everything, making plans 
    on how to conquer new avenues in space, how to feed themselves of stardust in order to achieve eternal life...
    as for biblical prediction, the Star od David turned into a black hole, ruining all plans of the inhabitants of the Coffee Way
    and messing up with their timeline. 

    You've got the chance to fix this, by going on a mission to fix your timeline, and ultimately safe life on the Coffee Way
    Be brave, and be careful, there are consequences for mistakes here in open space, and we wish you to never have to face them!

    To begin with. you should consult the cosmic map provided...


                               ~+

                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
                                 
                                 
    """)
    print("""
                                                                                `. ___
                                                                            __,' __`.                _..----....____
                                                                __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
                                                        _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
                                                        ,'________________                          \`-._`-','
                                                        `._              ```````````------...___   '-.._'-:
                                                            ```--.._      ,.                     ````--...__\-.
                                                                    `.--. `-`                       ____    |  |`
                                                                    `. `.                       ,'`````.  ;  ;`
                                                                        `._`.        __________   `.      \'__/`
                                                                        `-:._____/______/___/____`.     \  `
                                                                                    |       `._    `.    \
                                                                                    `._________`-.   `.   `.___
                                                                                                     `------'`
    """)
    print("please consult the map to proceed")


    map_var = input("Write Map to consult the map:  ")
    if map_var.lower() == "map":
        map()
    else:
        print("""
                            What are you going to do then? You better start over!!!!""")
        print("""
                                                        |
                                                        |
                                                        |
                                                        V
        """)

        start()


def map ():
    global nebular
    global andromeda
    global m42
    nebular = "Nebular Portal"
    andromeda = "Andromeda Portal"
    m42 = "M42 Portal"

    print("----------------------------------------------------")
    print("                 I                  I             ")
    print("----------------------------------------------------")
    print(f"  {nebular} I {andromeda} I  {m42}  ")
    print("----------------------------------------------------")
    print("                 I                  I             ")
    print("----------------------------------------------------")
    
    portal_choice()

def map_2():
    global nebular
    global andromeda
    global m42
    nebular = "Nebular Portal"
    andromeda = "Andromeda Portal"
    m42 = "M42 Portal"

    print("----------------------------------------------------")
    print("                 I                  I             ")
    print("----------------------------------------------------")
    print(f"  {nebular} I {andromeda} I  {m42}  ")
    print("----------------------------------------------------")
    print("                 I                  I             ")
    print("----------------------------------------------------")
    

def portal_choice():
    print("As you can see from the map, you have three life defining options. Each portal will bring you to three different realities...")
    print("Choose wisely, and remember time is on your hands")
    choice = input("What's your choice of portal? Please type nebular,andromeda, or m42:  ")
    if choice.lower() == "nebular":
        nebular_choice()
    elif choice.lower() == "andromeda":
        andromeda_choice()
    elif choice.lower() == "m42":
        m42_choice()
    else: 
        try_again = input("It seems like you are struggling to make a choice, or maybe mispelling a few words... To continue please type Return:   " )
        if try_again.lower == "return":
            portal_choice()
        else:
            print("""
            
            Please make a choice!

            S
            T
            A
            R
            T

            O
            V
            E
            R

            this time for real!

            |
            |
            |
            V
            """)
            portal_choice_2()
            
def portal_choice_2():
    print("As you can see from the map, you have three life defining options. Each portal will bring you to three different realities...")

    print("Now please, make your choice for real!")
    map_2()
    choice = input("What's your choice of portal? Please type nebular,andromeda, or m42:  ")
    if choice.lower() == "nebular":
        nebular_choice()
    elif choice.lower() == "andromeda":
        andromeda_choice()
    elif choice.lower() == "m42":
        m42_choice()
    else: 
        print("""
            
            ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
            ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
            ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
            ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
            ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
            ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
            ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
            ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
            ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
            ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
            ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
            ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
            ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
            ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼


            
            
            """)


        

def nebular_choice():
    print("""
    
                _                                  
              (`  ).                   _           
             (     ).              .:(`  )`.       
)           _(       '`.          :(   .    )      
        .=(`(      .   )     .--  `.  (    ) )      
       ((    (..__.:'-'   .+(   )   ` _`  ) )                 
`.     `(       ) )       (   .  )     (   )  ._   
  )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
)  )  ( )       --'       `- __.'         :(      )) 
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'          
                                        
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.

    You are finding yourself onto a mail universe... """)
    print("You might wonder what this is about... ")
    print("In this universe planet runs entirely on communication ")
    print("You can consult the map and make a choice on what planet you would like to visit")
    nebular_var = input("if you wish to consult the nebular map, just digit Nebular Map:  ")
    global ups
    global dhl
    global hermes
    ups = "UPS"
    dhl = "DHL"
    hermes = "Hermes"


    if nebular_var.lower() == "nebular map":
        nebular_map()
    else:
        try_again = input("Have you lost your mind already or did you just changed your plans? To continue please type Return:   " )
        if try_again.lower() == "return":
            return_to_portal()
        else:
            print("""
            In case you didn't get it, you have to make a choice! Right here, right now! Let's try again...
            |
            |
            |
            V""")
            nebular_choice()


def nebular_map():
    global ups
    global dhl
    global hermes

    print("----------------------------------------------------")
    print(f"               I    {nebular}  I             ")
    print("----------------------------------------------------")
    print(f"       {ups}     I      {dhl}           I     {hermes}  ")
    print("----------------------------------------------------")
    print("               I                    I             ")
    print("----------------------------------------------------")
    nebular_planets_choice()

def return_to_portal():
    print("""

    It seems like you got lost or simply mispelled your way into your chosen reality...
    Just in case let's make sure you are right on track...

    Please choose again what planet you would like to visit
    
    """)
    portal_choice_2()

def andromeda_choice():
    print("""
    
                              .--.---.
                            _ |||||||| _
                            \\\  |   |//
                             \_   \  ./
                  .--.         \   \/           .--.
                  ||||_        /\.  `\         _||||
                  |  ||      ./  /\   \        ||  |
                  |  /     ./   /  \   `\      \   |
                  |  |    /    /    `\   \      \  |
      .--.        |  |   /   ./  ___  \   \     |  |       .--.
     //| \        |  |   |   |.-'''\``\\   |    |  |       / |\\
     \\\| \       |  |   |   /    __|__|   |    |  |      /  ///
      ``\  \      |  |   |  `.   /     \   |    |  |     /  /''
         \  \     `   \  |   |(\/ o  o |   |   /   '    /  .'
         `   `     \   \ |   |`\    u  |   | ./   /    /   /
          \   `_    \   `\    \ \  -- /    |/    /    /   /
           \    `---.\    \    \/`-._/\   //    /   _/   /
            \_        `  _-    /       ` .-  .-----'    /
              `---.___ /'                     \        /
                     ./                        \------'
                    /    .-'|            |/\    \
                 _./    /'  /             \ `\   `-.
            __.-'     /'   |  o   |  \   o |  `\    `-._
    ____.--'     __.-'      \____/    \___/     `_._    `--._____
   /===.____.---'            |           |          `----.____===\
                             \           /
                             |           |
                             /           \
                            |             |
                           /              \ __.-----.__
                       ____--           -'  ___.       )
                   _.-'          \    /  _-'           /
                 ./     _.-_._  __/-./--'          _.-'
                 (            `-.______     ___.--'/
                  \_                   `---'  ___/'
                    `--._______.---------:F_P:'

    You are finding yourself onto an ancient Greek mythologic universe... """)
    print("Here you will be tasked by three differen Olympic gods, they sit on three different planets ")
    print("In order to visit them and be assigned on your mission you have to choose which planet to visit ")
    print("You can consult the map and make your choice")
    andromeda_var = input("if you wish to consult the andromeda map, just digit Andromeda Map:  ")
    global zeus
    global apollo
    global hermes
    zeus = "Zeus"
    apollo = "Apollo"
    hermes = "Hermes"

    if andromeda_var.lower() == "andromeda map":
        andromeda_map()
    else:
        try_again = input("Have you lost your mind already or did you just change your plans? To continue please type Return:   " )
        if try_again.lower() == "return":
            return_to_portal()
        else:
            print("""
            Please make a choice!

             Would you? 

              Pretty please???

                hm?  <3 <3 <3

              Let's try again...

                     |
                     |
                     |
                     V
            """)
            andromeda_choice()

def m42_choice():
    print("""
    
    You are finding yourself onto a Milky way universe... 
    
    o               .    ___---___                    .                   
       .              .--\        --.     .     .         .
                    ./.;_.\     __/~ \.     
                   /;  / `-'  __\    . \                            
 .        .       / ,--'     / .   .;   \        |
                 | .|       /       __   |      -O-       .
                |__/    __ |  . ;   \ | . |      |
                |      /  \\_    . ;| \___|    
   .    o       |      \  .~\\___,--'     |           .
                 |     | . ; ~~~~\_    __|
    |             \    \   .  .  ; \  /_/   .
   -O-        .    \   /         . |  ~/                  .
    |    .          ~\ \   .      /  /~          o
  .                   ~--___ ; ___--~       
                 .          ---         .              

    """)
    print("Here you will have the amazing opportunity to go on a mission on three planets ")
    print("In order to choose which planet to visit ")
    print("You can consult the map and make your choice")
    m42_var = input("if you wish to consult the M42 map, just digit M42 Map:  ")
    global moon
    global apollo
    global mars
    moon = "Moon"
    apollo = "Apollo"
    mars = "Mars"

    if m42_var.lower() == "m42 map":
        m42_map()
    else:
        try_again = input("Have you lost your mind already or did you just changed your plans? To continue please type Return:   " )
        if try_again.lower == "return":
            return_to_portal()
        else:
            print("""
            Please make a choice! Do we need to...

                p  e
             s      l
                    l
                   i
                 t
                o
               u
               t
               f
               o
               
               r

              YOU
               ?
            Come on, you can do it!
                      |
                      |
                      |
                      V
            """)
            m42_choice()



def andromeda_map():

    global zeus
    global apollo
    global hermes

    print("---------------------------------------------------------")
    print(f"                 I    {andromeda}   I             ")
    print("---------------------------------------------------------")
    print(f"       {hermes}    I        {zeus}           I    {apollo}  ")
    print("---------------------------------------------------------")
    print("                 I                       I             ")
    print("---------------------------------------------------------")
    andromeda_planets_choice()

def m42_map():

    global moon
    global apollo
    global mars

    print("----------------------------------------------------")
    print(f"                 I    {m42}    I             ")
    print("----------------------------------------------------")
    print(f"       {apollo}    I      {moon}        I    {mars}  ")
    print("----------------------------------------------------")
    print("                 I                  I             ")
    print("----------------------------------------------------")
    m42_planets_choice()


def nebular_planets_choice():
    print("""
    
    Now, you will be assigned on a mission depending what planet you choose to visit...
    Bear in mind that it's important for you to succeed in this mission in order to fulfil your purpose 
    of realigning the timeline of the Coffee Way, and save its inhabitants...
    
                     
    """)
    
    choice = input("the choice is in your hands: What planet would you like to visit? Please type UPS, DHL, or Hermes:  ")
    if choice.lower() == "ups":
        call_ups()
    elif choice.lower() == "dhl":
        call_dhl()
    elif choice.lower() == "hermes":
        call_hermes()
    else: 
        try_again = input("It seems like you are struggling to make a choice, or maybe mispelling a few words... To continue please type Return:   " )
        if try_again.lower == "return":
            nebular_planets_choice()
        else:
            print("""
            
            You have to make a choice if you want to save the Coffee way, 
            you arrived so far, be brave and continue your mission! Try again
                                        |
                                        |
                                        |
                                        V """)
            nebular_planets_choice()
        

    

def andromeda_planets_choice():
    print("""
    
    Now, you will visit one of the three planets of the Adromeda universe, and meet the respective gods...
    Hermes, Zeus or Apollo willl assign you to a mission, to help you 
    realigning the timeline of the Coffee Way, and save its inhabitants...

    Please be careful, and brave!
    
                     
    """)
    
    choice = input("the choice is in your hands: What planet would you like to visit? Please type Hermes, Zeus, or Apollo:  ")
    if choice.lower() == "hermes":
        call_hermes()
    elif choice.lower() == "zeus":
        call_zeus()
    elif choice.lower() == "apollo":
        call_apollo()
    else: 
        try_again = input("It seems like you are struggling to make a choice, or maybe mispelling a few words... To continue please type Return:   " )
        if try_again.lower == "return":
            andromeda_planets_choice()
        else:
            print("""
            
            You have to make a choice if you want to save the Coffee way, 
            you arrived so far, be brave and continue your mission! Try again
                                        |
                                        |
                                        |
                                        V """)
            andromeda_planets_choice()
        

def m42_planets_choice():
    print("""
    
    You are about to land on one of the three most scenographic planets of the solar system: Apollo, the Moon, and Mars
    Each one of them has a mission waiting for you. Choose wisely and follow the instructions of your mission, to make
    sure you fulfill your purpose of realigning your timeline, saving the Cofee Way, and safely return home!
                     
    """)
    
    choice = input("the choice is in your hands: What planet would you like to visit? Please type Apollo, Moon, or Mars:  ")
    if choice.lower() == "apollo":
        call_apollo()
    elif choice.lower() == "moon":
        call_moon()
    elif choice.lower() == "mars":
        call_mars()
    else: 
        try_again = input("It seems like you are struggling to make a choice, or maybe mispelling a few words... To continue please type Return:   " )
        if try_again.lower == "return":
            andromeda_planets_choice()
        else:
            print("""
            
            You have to make a choice if you want to save the Coffee way, 
            you arrived so far, be brave and continue your mission! Try again
                                        |
                                        |
                                        |
                                        V """)
            m42_planets_choice()
        




def call_moon():
    print("""
    
    
    Welcome to the mission on the moon traveller!
​
                      ___---___                    
                  .--           --.      
                ./   ()        .-. \.
               /   o     .    (   )  |
              / .              '-'     \         
             |  ()     .  O          .  |      
            |                            |      
            |     o             ()       |
            |         .--.           O   |            
             |   .   |    |             |
              \      `.__.'     o    . /    
               \                      /                   
                `\  o     ()        /'          
                  ```--___   ___--'`
                          ---
​
    
    This mission is a bit different from the others, as we ask you to sit and think about
    the work you have done so far... to enter a reflective state
    to face and embrace your weaknesses and your strenghts. Take your time, time here is timeless...
    and once you are ready, just press any key to go ahead on your journey...
    Remember you are a child of the universe, and you are always welcome to return to this space to find yourself again!
    """)
    input("Please enter a key, any key, it really doesn't matter, what it matters is yourself: ")

    happy_ending()



def call_hermes():
    print("Hermes : Welcome traveller, you've stumbled onto the most reliable mail planet of all, the GREAT HERMES!")
    print("To move through time and space to save the Coffee Way you must guess my reference number HAHAHA!")
    print("If you fail however, your mail will forever arrive past the delivery slot time and you will be the laughing stock of the greek gods.")
    print("""
    """)
    print("NOW TEST ME MORTAL IF YOU WISH TO ENTER THE NEXT PORTAL!")
    print("""
    """)
    import random 
    number = random.randint(1,10)
    for i in range(0,3):
        user = int(input("Guess a number between 1 and 10... Who knows if I will be fair... AHAHAHAHAH: "))
        if user == number:
            print("Well what can i say? You've bested me,..errmm,.. hurray..")
            print(f"you guessed the number right it's {number}")
            happy_ending()
            break
        elif user>number:
            print("your guess is too high, haha are you going to cry? Sadly you failed your mission!")
            end_noend()
            break
        elif user<number:
            print("your number is too low, what is the matter, is it time for you to go? I think so, sadly you failed your mission.")
            end_noend()
            break
        else:
            print(f"You have angered me and the time line gods, be gone with you foul mortal and enjoy your pergatory!")
            end_noend()
            break 


def call_dhl():
    print("Welcome traveller, you've stumbbled into my mail room of mahem")
    print("if you wish to continue the good fight you must first best me in a duel")
    print("a duel so terrible and evil only one champion has ever gotten the best of me")
    print("the man in question is Zeus king of gods but maybe that is an adventure for another day.....")
    print("""
    """)
    print("NOW KNEEL BEFORE ME! FOR I SHALL MAKE SURE YOU NEVER RECIEVE YOUR MAIL AGAIN!")
    print("""
    """)
    import random
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    cpu_score = 0
    player_score = 0
    player = False
    
    count = 1
    while True:
        player = input("Rock, Paper or  Scissors?").capitalize()
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                cpu_score+=1
            else:
                print("You win!", player, "smashes", computer)
                cpu_score+=1
                print("Congratulations! You have bested me the GREAT mail room manager of DHL, for that you may have your post and continue")
                happy_ending()
                break
                
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                cpu_score+=1
            else:
                print("You win!", player, "covers", computer)
                cpu_score+=1
                print("Congratulations! You have bested me the GREAT mail room manager of DHL, for that you may have your post and continue")
                happy_ending()
                break
               
                
                print("Congratulations! You have bested me the GREAT mail room manager of DHL, for that you may have your post and continue")
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                cpu_score+=1
            else:
                print("You win!", player, "cut", computer)
                cpu_score+=1
                print("Congratulations! You have bested me the GREAT mail room manager of DHL, for that you may have your post and continue")
                happy_ending()
                break
                
               
                
        elif player == 'E':
            print("Final Scores:")
            print(f"CPU:{cpu_score}")
            print(f"Plaer:{player_score}")
            break
        else:
            print("That's not a valid play. Check your spelling or else you'll recieve post on sundays!")
        count += 1
        if count == 4:
            print("Sorry you have exhausted all your chances and my patience, BE GONE FOUL BEING! SHOO SHOO!")
           
            end_noend()
            break
    
    computer = random.choice(choices)

def call_zeus():
    global name
    print("welcome to the zeus mission soldier, are you ready.")
    name = input("what is your name soldier  ")
    print(f"{name}! what a good choice soldier")
    zeus_start()

def zeus_start():
    global score_zeus
    global questions_zeus
    score_zeus = 0
    questions_zeus = 3
    print("""
      
                     .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __ 
      
      
      """)
    print(" do you accept the mission soldier? You better do! Let's start!")
    
    answer = input("who is zeus? ")
    if answer == ("the god of the sky"):
        score_zeus+=1
        print("correct")
        answer1()
    else:
        print("wrong answer")
        answer1()
        
        
def answer1():
    global score_zeus
    answer = input("was zeus the most powerful greek god")
    if answer == ("yes"):
        score_zeus+=1
        print("correct")
        answer2()
    else:
        print("wrong answer soldier")
        answer2()
        

def answer2():
    global score_zeus
    answer = input("did zeus ever shoot a bolt of lightning? ")
    if answer == ("yes"):
        score_zeus+=1
        print("correct")
        end_call_zeus()
    else:
        print("Wrong answer")
        end_call_zeus()


def end_call_zeus():
    global questions_zeus
    print(f"Your mission ends here, {name}!")
    print("rest now, soldier...")  
    print("Thank you for taking on this mission on UPS, you attempted",score_zeus,"questions correctly!")
    mark=(score_zeus/questions_zeus)*3
    print("Marks obtained:",mark)
    if mark >= 2:
        print("Congratulations! You managed to succed in your mission!")
        happy_ending()
    else:
        print("Unfortunately you scored too low and you didn't managed to succed in your mission :( ")
        end_noend()



def call_apollo():
    print("Welcome Traveller you have traversed through space and time to find yourself on the planet of Apollo.")
    print("To complete this task and speak to Apollo you must find the key word to this poem.")
    print("""
    """)
    print("Archimedes Said eureka,")
    print("Cos In English He Weren't Too Aversed In,")
    print("When He Discovered That The Volume Of A Body In The Bath,")
    print("Is Equal To The Stuff It Is Immersed In,")
    print("That Is The law Of Displacement,")
    print("Thats Why Ships Don't Sink,")
    print("Its A Shame He Weren't Around In 1912,")
    print("The Titanic Would Have Made Him Think.")
    
    words = "eureka"
    
    word = (words)
    print("""
    Find the lower case word""")
    
    guesses = ""
    turns = 3
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
                
            else:
                print("_")
                failed += 1             
        if failed == 0:
            print("You Win")
            
            
            print("The word is: ", word)
            print("""
            """)
            print("""

            Apollo : Well done traveller! 
            You may gaze upon my godly figure for you have completed the task!
            You have also managed to realign the timeline of your universe and to save
            the Coffee Way!
            You can return safely to your universe and enjoy your victory!

             """)
            happy_ending() 
            break
        guess = input("guess the word:").lower()
        guesses += guess
        if guess not in word:
            
            turns -= 1
            print("You have guessed wrong, but there maybe letters you have discovered that will help you")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("""
                
                    Sadly, you loose.
                    You will be directed to the Court of The Universe, 
                    they will decide there about your destiny
                    
                    """)
                end_noend()


def call_ups():
    global score_ups
    global name
    global questions
    score_ups = 0
    questions = 3
    print("""
      
          ~+
​
                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
      
      """)
    print("welcome to the ups mission ")
    name = input(" what is you name  soldier? ")
    print(f"{name}! a fine name for a soldier ")
    choice1()
    
def choice1():
    global score_ups
    answer = input("are you ready to accept the challenge? please type yes to accept the challange ")
    if answer.lower() == "yes":
        answer = input("when was ups founded ")
        if answer == ("1907"):
            score_ups+=1
            print("correct")
            choice2()

        else:
            print("wrong answer ")
            choice2()
    else:
        print("You better be ready! The only way out is through! Let's try again!")
        choice1()
    
    
def choice2():
    global score_ups
    answer = input("what does ups stand for? ")
    if answer.lower() == "united parcel service":
        print("correct")
        score_ups+=1
        choice3()
    else:
        print("wrong answer!!!")
        choice3()


def choice3():
    global score_ups
    answer = input("what service does ups offer? ")
    if answer.lower() == "mail service":
        print("correct !!!")
        print("thank you for playing good bye")
        score_ups+=1
        end()
    else:
        print("wrong answer sucka !!!")
        end()
     
     
     
     
def end():
    print(f"Your mission ends here, {name}!")
    print("rest now, soldier...")  

    print("Thank you for taking on this mission on UPS, you attempted",score_ups,"questions correctly!")
    mark=(score_ups/questions)*3
    print("Marks obtained:",mark)
    if mark >= 2:
        print("Congratulations! You managed to succed in your mission!")
        happy_ending()
    else:
        print("Unfortunately you scored too low and you didn't managed to succed in your mission :( ")
        end_noend()


def call_mars():
    import time
    print("""
    Welcome to the Mars Mission. In order to succeed and save the Coffee Way,
     you need to solve this...
​
​
              _________
             /___   ___|
            //@@@\ /@@@||
            \|@@@/ \@@@//
             \___ " ___/
                | - |
                 \_/
​
     """)
    time.sleep(1)
    # wait for 1 second
    game()

def game():
    global score
    global total_questions
    score=0
    total_questions=3
    
    print("Are you ready to play the Mission ? Please answer the following questions")
    
    
    answer = input("Question 1: What is the name of the science in charge with studying Mars?")

    if answer.lower()=="areography":
        score += 1
        print("""
    Well done, one in the bag!
    ​
             /\_/\  (
            ( ^.^ ) _)
             \``/  (
             ( | | )
            (__d b__)
    """)
    else:
        print("""
        _ 
        / ) 
    / /  
    / /               /\ 
    / /     .-```-.   / ^`-.  
    \ \    /       \_/  (|) `o 
    \ \  /   .-.   || _  ,--' 
    \ \/   /   )   \( `^^^  
        \   \/    (    )  
        \   )     )  /     
            ) /__    | (__  
        (___)))   (__)))
    ​
        Wrong answer!
    """)


    answer = input("Question 2: How else is Mars know as? ")
    if answer.lower()=="the red planet":
        score += 1
        print("""
    Good job, two down one to go!
    ​
    ​
         /\___/\`
        /       |
       |  o   o  |
     --|----*----|--
        \   w   /  
         =======
        /       \ __
        l        l\ \,
        l        l/ / 
        l  l l   / /
        \ m| |m /_/
    """)
    else:
        print("""
    No No No!!!
    ​
        ,-""""""-.
    /\j__/\  (  \`--.
    \`@_@'/  _)  >--.`.
    _{).:Y:_}_((_,'    ) )
    (_}`-^{_) ```     (_/
    ​
    """)
    answer = input("Question 3: What would the habitants of Mars be called? ")
    if answer.lower()=="martians":
        score += 1
        print("""Yeyy, you did it!
    ​
            ./\     /\.
            {  `---'  }
            {  O   O  }
            ~~>  V  <~~
             \  \|/  /
               ----'____
            /     \    \_
            {       }\  )_\_   _
            |  \_/  |/ /  \_\_/ )
            \__/  /(_/     \__/
                (__/
    """)
    else:
        print("""
    Really?
                            /^--^\     /^--^\     /^--^\|
                            \____/     \____/     \____/
                            /      \|  /      \|  /      \|
                           |        | |        | |        |
                            \__  __/   \__  __/   \__  __/
        |^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^\ \^|^|^|^|^|^|^|^|^|^|^|^|
        | | | | | | | | | | | | |\ \| | |/ /| | | | | | \ \ | | | | | | | | | | |
        ########################/ /######\ \###########/ /#######################
        | | | | | | | | | | | | \/| | | | \/| | | | | |\/ | | | | | | | | | | | |
        |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
    """)
    print("Thank you for Playing this small mission, you attempted",score,"questions correctly!")
    
    mark = (score/total_questions)*3
    print("Marks obtained:",mark)

    if mark >= 2:
        print("Congratulations! You managed to succed in your mission!")
        happy_ending()
    else:
        print("Unfortunately you scored to low and you didn't managed to succed in your mission :( ")
        end_noend()


def end_noend():
    import time

    print("""
    Hello traveler,
​
    you have reached the end of your journey here in space. Whilst you have tried
    your best, it was not enough to pass all the hard missions.
​
​
    You might be wondering what is happening to you now:
    you are now floating in space, slowly becoming part of it. One atom
    at a time, your bones are losing strength!
​
    From here on now, you are left without choices.....
    """)
    time.sleep(10)
    print("""
    
   ."          ".
  | .   `      ` |
  \(            )/
   \)__.    _._(/
   //   >..<   \\
   |__.' vv '.__/
      l'''"''l
      \_    _/
 _      )--(     _
​
    """)
    time.sleep(3)
    
    print("""
     _____                     _                                        __ _             _          _           _            _ _ _ 
    |_   _|                   | |                                      / _(_)           | |        | |         (_)          | | | |
      | |      _ __ ___   __ _| | _____     _   _  ___  _   _ _ __    | |_ _ _ __   __ _| |     ___| |__   ___  _  ___ ___  | | | |
      | |     | '_ ` _ \ / _` | |/ / _ \   | | | |/ _ \| | | | '__|   |  _| | '_ \ / _` | |    / __| '_ \ / _ \| |/ __/ _ \ | | | |
     _| |_    | | | | | | (_| |   <  __/   | |_| | (_) | |_| | |      | | | | | | | (_| | |   | (__| | | | (_) | | (_|  __/ |_|_|_|
    |_____|   |_| |_| |_|\__,_|_|\_\___|    \__, |\___/ \__,_|_|      |_| |_|_| |_|\__,_|_|    \___|_| |_|\___/|_|\___\___| (_|_|_)
                                            __/ |                                                                                 
                                            |___/                                                                                  
""")
    import random
    words = ["Reincarnated", "Universal material"]
    words = random.choice(words)
    print("You are now ", words)








def happy_ending():
    print("""
   ______                             __        __      __  _                 
  / ____/___  ____  ____ __________ _/ /___  __/ /___ _/ /_(_)___  ____  _____
 / /   / __ \/ __ \/ __ `/ ___/ __ `/ __/ / / / / __ `/ __/ / __ \/ __ \/ ___/
/ /___/ /_/ / / / / /_/ / /  / /_/ / /_/ /_/ / / /_/ / /_/ / /_/ / / / (__  ) 
\____/\____/_/ /_/\__, /_/   \__,_/\__/\__,_/_/\__,_/\__/_/\____/_/ /_/____/  
__  __           /____/      __            __                                 
\ \/ /___  __  __   | |     / /___  ____  / /                                 
 \  / __ \/ / / /   | | /| / / __ \/ __ \/ /                                  
 / / /_/ / /_/ /    | |/ |/ / /_/ / / / /_/                                   
/_/\____/\__,_/     |__/|__/\____/_/ /_(_)                                    
                                                                              

You managed to realign your timeline and to save the Coffee way, you are a hero!
Are you proud of yourself? You should be!
Now you can safely return back home... before that though we would like to thank you by offering
a dinner in our most exclusive restaurant, The Restaurant at the end of the Universe...
What would you like to do?
    """)
    decision()


def open_portal():
    print("""
        Goodbye brave traveller, have a safe journey home! We are going to miss you here!""")
    print("""

    ______________
    |\ ___________ /|
    | |  _ _ _ _  | |
    | | | | | | | | |
    | | |-+-+-+-| | |
    | | |-+-+=+%| | |
    | | |_|_|_|_| | |
    | |    ___    | |
    | |   [___] ()| |
    | |         ||| |
    | |         ()| |
    | |           | |
    | |           | |
    | |           | |
    |_|___________|_|

    """)
    door = input("Write enter to enter through the door: ")
    if door.lower() == "enter":
        print("""
    ______________
    |\ ___________ /|
    | |  /|,| |   | |
    | | |,x,| |   | |
    | | |,x,' |   | |
    | | |,x   ,   | |
    | | |/    |%==| |
    | |    /] ,   | |
    | |   [/ ()   | |
    | |       |   | |
    | |       |   | |
    | |       |   | |
    | |      ,'   | |
    | |   ,'      | |
    |_|,'_________|_|
        
        Buena vida! See you soon! :)

        """)
    else:
            print("""
            
            Wrong passcode traveller! Try again!""")
            open_portal()


def restaurant():
    print("""
    Welcome to the Restaurant at the end of the Universe...
    We've got a special menu for you, 
    """)
    menu_var = input("Digit menu to consult the menu:  ")
    if menu_var.lower() == "menu":
        menu()
    else:
        print("You have to consult the menu before being able to order it, let's start all over again!")
        restaurant()

def menu():
    print("""
    Here are our specialties:
    1. Pinaeapple Pizza
    2. Strawberry pizza
    3. Carbonara (authenthic italian recipe with no cream!)
    4. Espresso coffee
    What would you like to have?
    """)
    global food_order
    food_order = input("Please write your number of choice: ")
    order()

def order():
    if food_order == "1":
        print("""

                _______
            _,--~~    ~~--._
        ,/'  m%%%%%%=@%%m  `\.
        /' m%%o(_)%%o%%%%o%%m `|
        /' %%@=%o%%%o%%%o%(_)o%%%|
    /  %o%%%%%=@%%%(_)%%o%%@=%%  |
    |  (_)%(_)%%o%%%o%%%%=@(_)%%%  |
    | %%o%%%%o%%%(_)%%o%%o%%%%o%%% |
    | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
    |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
    \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
        \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
        \_ ~o%=@%(_)%o%%(_)%~ _/             
            `\_~~o%%%o%%%%%~~_/'
            `--..____,,--'     
                                                        \|/
                                                        AXA
                                                       /XXX|
                                                       \XXX/
                                                        `^'
    """)
    elif food_order == "2":
        print("""


                ____
            _,--~~    ~~--._
        ,/'  m%%%%%%=@%%m  `\.
        /' m%%o(_)%%o%%%%o%%m `|
        /' %%@=%o%%%o%%%o%(_)o%%%|
    /  %o%%%%%=@%%%(_)%%o%%@=%%  |
    |  (_)%(_)%%o%%%o%%%%=@(_)%%%  |
    | %%o%%%%o%%%(_)%%o%%o%%%%o%%% |
    | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
    |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
    \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
        \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
        \_ ~o%=@%(_)%o%%(_)%~ _/             
            `\_~~o%%%o%%%%%~~_/'
            `--..____,,--'     
        //
     _ || __
  .--\\`||/.'--.
 / .-'.- +\`-._V`.
JV `".'/||\\`-' V |
J VV  V  V  V   V |
 L V  V V V VV V V F
 |V V V  V  V  VV /
 J  V   V V  V  V/
  \V  V    V  V J
   L V  V  V  V F
   JV V  V  V V/
    \ V    V .'
     `-.V_.-'



        """)
    elif food_order == "3":
        print("""

                                        ██████████████                                      
                                ██████  ██░░░░▒▒▒▒▒▒▒▒░░██                                    
                            ██░░▒▒▒▒██▒▒████▒▒▒▒████████▓▓██████                            
                        ████▒▒▒▒████████▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                          
                    ▓▓████▒▒░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒████                        
            ██████░░▒▒▒▒▒▒▒▒▒▒████████████▒▒▒▒▒▒▓▓▓▓▒▒▒▒██░░░░████▒▒████▓▓██                
        ████▓▓▓▓██▓▓████▒▒▒▒▒▒██  ░░██░░██▒▒▒▒██  ▒▒██▒▒██░░  ░░░░████▒▒▓▓▓▓████            
    ████▒▒▒▒▒▒██▒▒▒▒▒▒▓▓▓▓▒▒██░░░░██  ░░██▒▒██░░██░░██▒▒▒▒██▒▒        ████▒▒▒▒▒▒████        
    ██▓▓▒▒▒▒▒▒██████▓▓▓▓▓▓████  ░░██░░░░██  ██░░░░██  ░░██▒▒██    ░░    ▒▒░░██▒▒▒▒▒▒▒▒██      
██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▓▓██░░░░██░░██░░██░░░░██░░██      ░░████        ▒▒    ██▒▒▒▒▒▒▒▒▒▒██    
██▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██░░░░████████████▓▓░░░░██  ▒▒░░    ░░░░  ▒▒  ░░        ██▒▒▒▒▒▒▒▒▓▓██  
██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▓▓██░░██░░░░░░░░░░░░░░████░░████    ▒▒                ░░  ██▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒██▒▒▓▓▓▓▓▓▓▓████░░░░██████████░░░░░░██░░░░██  ██████  ████  ▒▒      ██▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓██░░████░░██░░██░░██░░████░░░░░░██░░░░░░██░░██████  ▒▒  ██▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██████▓▓██░░██░░██░░██░░░░██░░░░████░░░░▒▒░░████▓▓▒▒▒▒  ██████▓▓▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██░░██  ██░░██  ████░░██░░░░██▓▓░░██░░░░██░░  ██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░▓▓  ██░░██░░  ██░░░░░░░░░░████████░░░░░░██▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒██  
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██  ░░▓▓░░██  ░░██░░░░░░▓▓████░░░░██░░██████▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒██    
    ▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████░░██  ░░██████████  ░░░░████░░██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒████      
        ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██░░░░██░░░░░░░░░░░░████  ░░░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒████          
            ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████████████████▓▓▓▓██████▓▓▒▒▒▒▒▒▒▒▒▒██████              
                ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████                    
                        ████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████                          
                                    ████████████████████                                      
                                                                                            
                                                            

        """)
    elif food_order == "4":
        print("""
     (  )   (   )  )
      ) (   )  (  (
      ( )  (    ) )
      _____________
     <_____________> ___
     |             |/ _ |
     |               | | |
     |               |_| |
  ___|             |\___/               
 /    \___________/    |
 \_____________________/


        
        
        """)
    else:
        print("""
            
            Wrong choice! Try again!""")
        menu()


    print("Would you like to order something else?")
    order_again = input("Please write yes or no: ")
    if order_again.lower() == "yes":
        menu()
    else:
        print("""
        
                    Thank you for having dined with us
                    We hope you enjoyed your meal,
                    See you again on your next adventure!
        """)
        open_portal()
#menu()
           



def decision():
    choice = input("Please write restaurant to go to dinner, and home to go home: ")
    if  choice.lower() == "home":
        open_portal()
    elif choice.lower() == "restaurant":
        restaurant()
    else:
        try_again = input("It seems like you are struggling to make a choice, or maybe mispelling a few words... To continue please type Return:   " )
        if try_again.lower == "return":
            happy_ending()
        else:
            print("Sorry but you have to make a choice! Let's start over!")
            happy_ending()



# pid = os.fork()          
# if pid == 0:
#     os.system("afplay music.mp3")
# else:
#     start()
start()



    


