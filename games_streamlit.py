import streamlit as st
import time
import random

#Home Page
st.title("Welcome to Games")
st.header("\n\nThere are a lot of games to play\n")
st.header("Select the game you want to play")

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if "mode" not in st.session_state:
    st.session_state.mode = None



if st.session_state.page=='home':
    if st.button("New User"):
        st.session_state.page = 'login'
        st.session_state.mode = 'new_user'
    if st.button("Old User"):
        st.session_state.page = 'login'
        st.session_state.mode = 'old_user'


#Login page
if st.session_state.mode == 'new_user':
    st.header("Welcome new user")
    id_ = st.text_input("Enter your id")
    pass_ = st.text_input("Enter your password")
    name = st.text_input("Enter your username")
    if st.button("Create Account"):
        with open('idpass.txt','a') as f:
            f.write(f"\n{id_},{pass_},{name}")
        st.success("Account created! Please login.")
        st.session_state.page = 'select_game'


elif st.session_state.mode=='old_user':
    id_check = pass_check = 0
    check = ""
    f = open('idpass.txt','r')
    st.write("Please Enter you id and password")
    id_=st.text_input("Enter your id")
    pass_=st.text_input("Enter your password",type='password')
    if st.button("Login"):
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
            st.session_state.page='select_game'
        else:
            st.error("Invalid id or password")
    f.close()


#Game Selection Page
if st.session_state.page=='select_game':
    if st.button("Number Guessing Game"):
        st.session_state.page='number_guessing_game'
    if st.button("Snake Water Gun"):
        st.session_state.page='snake_water_gun'
    if st.button("Hangman"):
        st.session_state.page='hangman'
    if st.button("Tic Tac Toe"):
        st.session_state.page='tic_tac_toe'


#Number Guessing Game
if st.session_state.page == 'number_guessing_game':
    st.header("Welcome to Number Guessing Game")
    if st.button("Game Rules"):
        st.write("In this game the computer will choose a number between 1 and 100 and you have to guess the number")
        st.write("If you guessed a higher number then the computer will tell you to enter a lower number")
        st.write("And if you guessed a lower number then the computer will tell you to enter a higher number")
        st.write("You will only have 10 chances to guess the number")
        st.write("You win if you guessed the right number in 10 chances ,else the computer will win")

    if 'comp_num' not in st.session_state:
        st.session_state.comp_num = random.randint(1,100)
        st.session_state.attempts = 0
        st.session_state.win = False

    guess = st.number_input("Enter your guess (1-100)", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.comp_num:
            st.success(f"You Won! You guessed in {st.session_state.attempts} attempts.")
            st.session_state.win = True
        elif guess > st.session_state.comp_num:
            st.info("Try a lower number.")
        else:
            st.info("Try a higher number.")

        if st.session_state.attempts >= 10 and not st.session_state.win:
            st.error(f"You Lose! The number was {st.session_state.comp_num}")
