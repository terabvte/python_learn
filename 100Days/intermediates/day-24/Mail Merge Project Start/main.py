#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
      

cwd = "../Input/Names/invited_names.txt"
abso = "./100Days/intermediates/day-24/Mail Merge Project Start/Output/"

# Read file

with open(abso+cwd) as file:
    lines = [line.rstrip() for line in file]
    
# Write file    
# TODO... gotta do german, check this for reference https://chatgpt.com/c/6727bb26-3570-8006-83ed-8d453fca1d17

with open(abso+"../Input/Letters/starting_letters.txt", mode="w+") as Letter_for_:
    letter = file.read()
    for line in lines:
        letter.replace("[name]", line)
        file.write()

