import random
import os
from os import system, name

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def removeBlank(termOrDef):
    try:
        if termOrDef[0] == "":
            termOrDef.pop(0)
        if termOrDef[len(termOrDef)-1] == "":
            termOrDef.pop(len(termOrDef)-1)
    except IndexError:
        return

termPath = os.path.expanduser("~/memberBerries/term.txt").replace("\\", "/").replace('"', "")
definitionPath = os.path.expanduser("~/memberBerries/definition.txt").replace("\\", "/").replace('"', "")

if not(os.path.isdir(os.path.expanduser("~/memberBerries"))):
    os.makedirs(os.path.expanduser("~/memberBerries"))

if not(os.path.isfile(os.path.expanduser(termPath))):
    termFile = open(os.path.expanduser(termPath), "w")

if not(os.path.isfile(os.path.expanduser(definitionPath))):
    definitionFile = open(os.path.expanduser(definitionPath), "w")

termFile = open(os.path.expanduser(termPath), "r")
termFile = termFile.read()
term = termFile.split("^")

definitionFile = open(os.path.expanduser(definitionPath), "r")
definitionFile = definitionFile.read()
definition = definitionFile.split("^")
removeBlank(term)
removeBlank(definition)
cardOrder = []

def add():
    clear()
    global term, definition, definitionPath, termPath
    termInput = input("Add your term\n>")
    term.append(termInput)
    definitionInput = input("Add your definition\n>")
    definition.append(definitionInput)

    if not(termInput) == "" and not(definitionInput == ""):
        termFile = open(os.path.expanduser(termPath),"a")
        termFile.write(f"^{termInput}")
        termFile = open(os.path.expanduser(termPath), "r")
        termFile = termFile.read()
        term = termFile.split("^")
        removeBlank(term)

        definitionFile = open(os.path.expanduser(definitionPath),"a")
        definitionFile.write(f"^{definitionInput}")
        definitionFile = open(os.path.expanduser(definitionPath), "r")
        definitionFile = definitionFile.read()
        definition = definitionFile.split("^")
        removeBlank(definition)

    else:
        clear()
        print("Did not add your card because it had a blank input.")
        input("Hit ENTER to continue!")

def remove():
    global term, definition, definitionPath, termPath
    clear()
    for i in range (0,len(term)):
        print(f"{i}: {term[i]}")
    remove = input("\nWhich card do you wish to remove? Write the number\n>")
    try:
        remove = int(remove)
        #Removes term
        term.pop(remove)
        for i in range (0,len(term)):
            print(f"- {term[i]}")
        termFile = open(os.path.expanduser(termPath), "w")
        for i in range (0,len(term)-1):
            termFile.write(f"{term[i]}^")
        termFile.write(term[len(term)-1])
        termFile.close()
        #Removes definition
        definition.pop(remove)
        definitionFile = open(os.path.expanduser(definitionPath), "w")
        for i in range (0,len(term)-1):
            definitionFile.write(f"{definition[i]}^")
        termFile.write(definition[len(definition)-1])
        termFile.close()
    except ValueError:
        clear()
        print("You need to choose a number from the list!")
        input("Hit ENTER to continue!")
    except IndexError:
        clear()
        print("You need to choose a number from the list!")
        input("Hit ENTER to continue!")

def member():
    global term, definition, definitionPath, termPath
    for i in range (0,len(term)):
            cardOrder.append(i)
    random.shuffle(cardOrder)
    for i in range (0,len(term)-1):
        if len(term) > 0:
            clear()
            currentCard = cardOrder[i]
            print(f"Member {term[currentCard]}?")
            input("Hit ENTER to see definition!")
            clear()
            print(f"I member {term[currentCard]} it's:\n{definition[currentCard]}\n")
            input("Hit ENTER to go to next card!")
            clear()
        else:
            clear()
            print("You don't have any cards to member, go add some!")
            input("Hit ENTER to continue!")

while True:
    clear()
    print("Welcome to Member Berries!")
    userInput = input("What do you want to do?\n (a)dd: add a new card to member\n (r)emove: remove a card you are done membering\n (m)ember: start membering!\n (ab)out: abount Member Berries\n (e)xit: exit Member Berries\n>").lower().strip()
    
    if userInput == "add" or userInput == "a":
        add()

    elif userInput == "remove" or userInput == "r":
        remove()

    elif userInput == "member" or userInput == "m":
        member()

    elif userInput == "about" or userInput == "ab":
        clear()
        print("Member Berries is a flash card application written in python named after member berries from South Park.\nIt is an easy and fun way to learn terms!\nMember us!")
        input("Hit ENTER to Continue!")

    elif userInput == "exit" or userInput == "e":
        clear()
        break

    else:
        print("You need to choose one of the options!")
        input("Hit ENTER to Continue!")

