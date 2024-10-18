invitees = ["Alan Turing", "Nikola Tesla", "Isaac Netwon"]

print(f"\nDear {invitees[0]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[1]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[2]}, you are invited to the Groundbreaking Dinner™!")

print(f"\nDue to unforeseen circumstances, it looks like {invitees.pop(1)} won't be joining us...")

invitees.insert(1, "George Washington")

print(f"\nDear {invitees[0]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[1]}, you are invited to the Groundbreaking Dinner™!")
print(f"Dear {invitees[2]}, you are invited to the Groundbreaking Dinner™!")