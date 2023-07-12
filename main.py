# this script will generate random character traits for a poggle in dnd

import random

alignmentl = ["Lawful", "Neutral", "Chaotic"]
alignmentr = ["Good", "Neutral", "Evil"]

backstorys = ["cowboy", "pirate", "doctor", "baker", "lawyer", "chef", "spy", "soldier", "teacher", "pilot",
              "police officer", "firefighter", "ninja", "viking", "knight", "wizard", "witch", "priest", "monk", "nun",
              "sailor", "farmer", "blacksmith", "miner", "architect", "engineer", "artist", "musician", "actor",
              "athlete", "scientist", "inventor", "detective", "writer", "journalist", "politician", "businessperson",
              "entrepreneur", "philosopher", "scholar", "student"]

accents = ["Posh", "Wild west", "Pirate", "Southern", "New York", "Boston", "Australian", "British", "Irish",
           "Scottish"]

possibleNames = []

for name in open("names"):
    possibleNames.append(name.strip())


def removeName(name):
    possibleNames.remove(name)

    file = open("names", "w")
    for n in possibleNames:
        file.write(n + "\n")

    file.close()

    file = open("usedNames", "a")
    file.write(name + "\n")
    file.close()


def create():
    if not possibleNames:
        print("You have used all of the names!")
        return

    name = random.choice(possibleNames)
    removeName(name)
    alignment = random.choice(alignmentl) + " " + random.choice(alignmentr)
    backstory = random.choice(backstorys)
    accent = random.choice(accents)

    print("You are a " + alignment + " " + backstory + " named " + name + "." + " You have a " + accent + " accent.")

    lifeRoll = random.randint(1, 20)

    if lifeRoll < 10:
        amnesiaRoll = random.randint(1, 4)

        if lifeRoll == 1 and amnesiaRoll == 4:
            print("Your poggle will live its entire life not knowing who they are, where they came from, or what will happen to them.")
        else:
            print(f"Your poggle will live for {lifeRoll + 3} hours and will have amnesia for {amnesiaRoll} hours.")
    else:
        print(f"Your poggle will live for {lifeRoll + 3} hours, with no amnesia.")


create()
