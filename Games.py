# Module import
import time
import random


#Global Variables
name = ""


#Introduction
print("################# WELCOME TO GAMES #######################")
for i in range(1,6):
    time.sleep(0.5)
    print(".",end=' ')
time.sleep(2)
print("THIS CODE INCLUDES A LOT OF GAMES TO PLAY")
time.sleep(1)
input("PRESS ANY KEY TO GET STARTED")

#Sign-in/Log-in
user_type=input("Are you a new user or an old user.Type(new/old)")

#New user
if user_type.lower()=="new":
    f=open('idpass.txt','a')
    print("Hello new user")
    print("Please Create your id and password below")
    time.sleep(1)
    id_ = input("Create you id here")
    pass_ = input("Create your password")
    name = input("Enter you name")
    f.write(f"\n{id_},{pass_},{name}")
    time.sleep(0.8)
    print(f"Welcome {name}!")
    f.close()
    

#Old user
elif user_type.lower()=="old":
    id_check = pass_check = 0
    check = ""
    f=open('idpass.txt','r')
    print("Please Enter your id and password below")
    time.sleep(1)
    id_ = input("Enter your id")
    pass_ = input("Enter your password")
    while True:
        line=f.readline()
        if not line:
            break       
        check=line.split(",")
        if check[0]==id_:
            id_check=1
            if check[1]==pass_:
                pass_check=1
                break
            elif check[1]!=pass_:
                id_check=0
    name=check[2]
    if id_check==1 and pass_check==1:
        print(f"Welcome back {name}")
    else:
        raise ValueError("You have entered wrong id or password")
    f.close()
        



#Game selection
print("Please select the game you want to play")
print("S.NO                     NAME OF GAME")
print("----------------------+--------------------------")
print("1.                       Number Guessing Game")
print("----------------------+--------------------------")
print("2.                       Snake Water Gun")
print("----------------------+--------------------------")
print("3.                       HangMan")
print("----------------------+--------------------------")
game=int(input("Enter the S.no of the game you want to play"))


# Number Guessing Game
if game==1:
    #Game Rules
    print("########## Welcome to Number Guessing Game ##############")
    time.sleep(1)
    print("---------------GAME RULES-------------")
    print("In this game the computer will choose a number between 1 and 100 and you have to guess the number ")
    print("If you guessed a higher number then the computer will tell you to enter a lower number")
    print("And if you guessed a lower number then the computer will tell you to enter a higher number")
    print("You will only have 10 chances to guess the number")
    print("You win if you guessed the right number in 10 chances ,else the computer will win")
    time.sleep(3)
    input("Press any key to contiue")

    # Game Starts
    comp_num = random.randint(1,100)
    win = i = 0
    for i in range(1,11):
        if i == 1:
            user_num = int(input("Enter the Guessed number"))
        else:
            if user_num > comp_num:
                user_num = int(input("Please guess a lower number"))
            elif user_num < comp_num:
                user_num = int(input("Please guess a higher number"))
            else:
                win = 1
                break
    if win==0:
        print(f"You Loose,The number choosen by the computer was {comp_num}")
    elif win==1:
        print(f"You Won,You took {i-1} attempts to guess the correct number")


# Snake Water Gun
elif game==2:
    # Game Rules
    print("############## Welcome to Snake Water Gun ################")
    time.sleep(1)
    print("--------------GAME RULES----------------")
    print("This game has 3 elements --> 1.Snake(s) ,2.Water(w) ,3.Gun(g)")
    print("The computer will choose one of these and you will choose one of these")
    print("If Snake vs Water -> Snake wins , Snake vs Gun -> Gun wins , Water vs Gun -> Water wins")
    print("There will be 10 rounds and who wins the maximum rounds , wins the game")
    print("If a round is draw then no one gets point")
    print("If the game ends in a draw , a super-round will be held and the winner will be decided based on that super-round")
    time.sleep(3)
    input("Enter any key to continue")

    # Game starts
    comp_win = user_win = 0
    ui = ci = ""
    for i in range(1,11):
        rdnum = random.randint(1,100)   
        if rdnum <= 33:
            ci = "s"
        elif rdnum >33 and rdnum <=66:
            ci = "w"
        else:
            ci = "g"
        print("The computer has choosen ,Now your turn to choose")
        ui = input("Choose (s/w/g)")
        if (ui.lower()=="s" and ci == "w") or (ui.lower()=="w" and ci == "g") or (ui.lower()=="g" and ci=="s"):
            print(f"You chose {ui} and computer chose {ci}")
            print("So you won this round")
            user_win = user_win + 1
        elif (ci.lower()=="s" and ui == "w") or (ci.lower()=="w" and ui == "g") or (ci.lower()=="g" and ui=="s"):
            print(f"You chose {ui} and computer chose {ci}")
            print("So computer won this round")
            comp_win = comp_win + 1
        else:
            print(f"You chose {ui} and computer chose {ci}")
            print("So no one won this round")
        print("\n\n")
        time.sleep(2.3)
    print("! ! GAME OVER ! !")
    time.sleep(1)
    print("Processing...")
    for i in range(1,6):
        print(".")
        time.sleep(0.5)
    if comp_win > user_win:
        print("COMPUTER WON THE GAME")
    elif comp_win < user_win:
        print("YOU WON THE GAME")
    else:
        print("GAME ENDED IN A DRAW")
        time.sleep(2)
        input("Get Ready for Super-Round !,Press any key to continue")
        user_win = comp_win = 0
        ui = ci = ""
        draw = 1
        while draw == 1:
            rdnum = random.randint(1,100)
            if rdnum <= 33:
                ci = "s"
            elif rdnum >33 and rdnum <=66:
                ci = "w"
            else:
                ci = "g"
            ui = input("Choose (s/w/g)")
            if (ui.lower()=="s" and ci == "w") or (ui.lower()=="w" and ci == "g") or (ui.lower()=="g" and ci=="s"):
                print(f"You chose {ui} and computer chose {ci}")
                print("So you won this round")
                user_win = user_win + 1
            elif (ci.lower()=="s" and ui == "w") or (ci.lower()=="w" and ui == "g") or (ci.lower()=="g" and ui=="s"):
                print(f"You chose {ui} and computer chose {ci}")
                print("So computer won this round")
                comp_win = comp_win + 1
            else:
                print(f"You chose {ui} and computer chose {ci}")
                print("So no one won this round")
            if comp_win > user_win:
                print("COMPUTER WON THE GAME")
                break
            elif comp_win < user_win:
                print("YOU WON THE GAME")
                break
            elif comp_win == user_win:
                print("Game drawed again , So a next super-round will be held")
                draw = 1


#HangMan
if game==3:
    #Rules
    print("#################### WELCOME TO HANGMAN ##########################")
    time.sleep(1)
    print("In this game the computer will choose a word and you have to guess that word letter by letter")
    print("You will have 5 chances only")
    print("If you guessed all the letter of that word in 5 chances , you win the game ,else the computer wins ")
    print("The length of the words increases based on the difficulty level choosen")

    print("CHOOSE A DIFFICULTY LEVEL")
    print("----------easy(e)-----------medium(m)-------------hard(h)--------------")
    level = input("Enter the difficulty level (e/m/h)")
    for i in range (4):
        time.sleep(0.5)
        print(".",end=' ')
    if level.lower()=="e":
        words=["am","an","cut","at","ace","bad","can","ear","had","dye"]
    elif level.lower()=="m":
        words=["apple","bread","chair","dance","eagle","fire","grape","horse","jump","kite"]
    elif level.lower()=="h":
        words=["abacus","balance","cabinet","decide","feature","harmony","justice","monitor","picture","special"]
    else:
        words=["am","an","cut","at","ace","bad","can","ear","had","dye"]
    num = random.randint(1,10)
    word = words[num]
    chances = 5
    word_length = len(word)
    alphabets = list(word)
    guessed_letter = []
    for i in range (0,word_length):
        guessed_letter.append("_")

    print(f"This is the word -> {guessed_letter}\n")
    while chances>=1:
        print("Choose your letter")
        letter = input("Enter the letter which you think is in the word")
        condition = letter in alphabets
        if condition == True:
            print(f"\n\nNice Guess!,The letter '{letter}' was present in the word")
            for i,alphabet in enumerate(alphabets):
                if letter == alphabet:
                    guessed_letter[i] = letter
                time.sleep(1.7)
            print(f"Now the word is -> {guessed_letter}")
        else:
            print(f"\nOOPS! Wrong Guess , The letter '{letter}' is not present in the word")
            chances = chances - 1
        print(f"Chances left = {chances}")
        print("\n\n")
    if guessed_letter == alphabets :
        print("Nice! YOU WON")
        print("\n")
    elif guessed_letter != alphabets:
        print("\nCOMPUTER WON")



# Conclusion
time.sleep(1)
print("THAKYOU FOR PLAYING THE GAMES ,HOPE YOU ENJOYED")

    

