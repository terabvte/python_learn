# Original code

invitees = ["Alan Turing", "Nikola Tesla", "Isaac Netwon"]

print(f"\nDear {invitees[0]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[1]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[2]}, you are invited to the Groundbreaking Dinner™!")

# Changes to the guests..

print(f"\nDue to unforeseen circumstances, it looks like {invitees.pop(1)} won't be joining us...")

invitees.insert(1, "George Washington")

print(f"\nDear {invitees[0]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[1]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[2]}, you are invited to the Groundbreaking Dinner™!")

# Bigger dinner table!!

print("\nA new, bigger dinner table has been located! More to come!!")

invitees.insert(0, "Napoleon Bonaparte")
invitees.insert(2, "Jeanne D'Arc")
invitees.append("Leonardo Da Vinci")

print(f"\nDear {invitees[0]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[1]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[2]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[3]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[4]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[5]}, you are invited to the Groundbreaking Dinner™!")

# Shrinking guest list...

print("\nUnfortunately, it has come to my attention that we may only invite TWO people to the Groundbreaking Dinner™...")

print(f"I'm sorry  {invitees.pop()} it looks like you're getting kicked...")
print(f"I'm sorry  {invitees.pop()} it looks like you're getting kicked...")
print(f"I'm sorry  {invitees.pop()} it looks like you're getting kicked...")
print(f"I'm sorry  {invitees.pop()} it looks like you're getting kicked...")

print(f"\nDear {invitees[0]}, I would like to let you know that you're still invited to the Groundbreaking Dinner™!")
print(f"\nDear {invitees[1]}, I would like to let you know that you're still invited to the Groundbreaking Dinner™!")

del invitees[0]
del invitees[0]

print (f"\n {invitees}")


