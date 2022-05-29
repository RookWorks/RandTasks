import random
import time

def printpause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)

def tasks (name, care, chore):
    while True:
        user_input = input("What is your name?")
        name.append(user_input)
        printpause ("Hello " +name+ " would you like help deciding what to do today?")
        if user_input == "care":
            printpause("" +care)
        if user_input == "chore":
            printpause("" +chore)


def run():
    name = []
    care = ([])
    chore = ([])
    tasks (name, care, chore)

run()
