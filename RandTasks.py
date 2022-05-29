import random
import time

def printpause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)

def tasks (name, care, chore):
    while True:
        user_input = input("What is your name?\n")
        if user_input != " ":
            name.extend(user_input)
        user_input = input("Hello " +(" ".join(name))+ " would you like help deciding" 
                        " what to do today?\n")
        if user_input == "care":
            printpause("Maybe you should " +care+ "?\n")
        elif user_input == "chore":
            printpause("What if you " +chore+ "?\n")
        playagain()

def playagain():
    again = input("Is that something you'd like to do? (y/n)\n")
    if again == "y":
        printpause("Happy to help! I'll be here if you need me.\n")
        quit()
    elif again == "n":
        printpause == ("Hmm, maybe I can think of something else?\n")
        run()

def run():
    name = []
    care = random.choice(["try to meditate for 30 minutes", "take a 30 minute cat nap", 
            "read or listen to an audio book", "take a short stroll", 
            "drink some water", "eat a snack", "message a friend"])
    chore = random.choice(["vaccum one room", "make your bed", "sweep the kitchen",
            "water your garden", "do your laundry", "clean your desk"])
    tasks (name, care, chore)

run()
