# Lesson 2: Assignments: Nested If

# 1. Nested Decisions: The Adventure Game 🏰

# Task 1: Code Correction

# Correct Code

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2: Setting the Scene + Task 3: Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:                                               # Task 3: Default Path
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You got lost!")
    else:                                               # Task 3: Default Path
       pass
else:                                                   # Task 3: Default Path
   pass


# 2. Quick Decisions: The Event Planner 🎉

# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
print("large hall") if attendees > 100 else print("conference room")

# Task 2: Venue Selection

print("audio system") if attendees > 100 else print("microphone")

# Task 3: Catering Choices

food = input("Do you want vegetarian food: yes or no? ")
print("Veggie Delight Caterers") if food == "yes" else print("Gourmet Meals Caterers")