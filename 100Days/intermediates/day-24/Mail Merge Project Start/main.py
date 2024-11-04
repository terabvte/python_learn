# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


cwd = "../Input/Names/invited_names.txt"
abso = "./100Days/intermediates/day-24/Mail Merge Project Start/Output/"

# Read file

with open(abso + cwd) as invited_names:
    names = [name.rstrip() for name in invited_names]

# Write file
# TODO... gotta do german, check this for reference https://chatgpt.com/c/6727bb26-3570-8006-83ed-8d453fca1d17
# update next day: debugged and solved this in like 15 minutes. running in the morning is OP

for name in names:

    with open(
        abso + "../Input/Letters/starting_letter.txt", mode="r"
    ) as starting_letter:
        letter = starting_letter.read()

    letter = letter.replace("[name]", name)
    with open(
        abso + f"./ReadyToSend/Letter_for_{name}.txt", mode="w+"
    ) as finished_letter:

        finished_letter.write(letter)
