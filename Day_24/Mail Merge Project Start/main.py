#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode="w") as file:
    sample = file.write(f"Dear [name],\n\nYou are invited to my birthday this Saturday. \n\nHope you can make it!\n\nJume")

with open("Input/Letters/starting_letter.txt") as file:
    sample = file.read()
    with open("Input/Names/invited_names.txt") as file:
        lines = file.readlines()
        for line in lines:
            with open(f"Output/ReadyToSend/invite_for_{line}.txt", mode="w") as invitation:
                invite = sample.replace("[name]", f"{line.strip()}")
                invitation.write(invite)