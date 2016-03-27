# Ben Sklar
# Program Function -> Guessing game with computer--computer tries to guess number.
# Uses prompts, input statements, print statements, /n, loops, etc.


# Asks for name to remember it.
print("Welcome to Guess the Number 2.0, where I, the computer, guess your number.")
name=input("What is your name? ")

# Tells you your name and tells the user that the computer's name is Olaf. Also includes picture of fictional Olaf.
print("Hello,", name + ". I am Olaf, a computer.")
print(
"""      
                 _______
               _/       \_
              / |       | \\
             /  |__   __|  \\
         (=)|__/(.)| |(.)\__|(=)
         (=)|      | |      |(=)
            |\     |_|     /|
            | \ /       \ / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
               |_|_____|_|
           ____|_________|____
          /                   \  
         /                     \\

""")

# Asks user to think of a number and tells user how to respond.
print("\nThink of a number between 1 and 100. \n\nI will try to guess the number in as few tries as possible.")
input("Please only respond with \"l\" for lower, \"h\" for higher, or \"y\" for yes. \n\nIf you understand, please press enter...")

# Establishes parameters between 1-100 for numbers, and guesses 50 to start. 50 halfway from 100.
low = 1
high = 100
response = ''
firstguess = 50
tries = 1

# Loop for guessing numbers. y=yes, h=higher, l=lower. y ends (breaks) the loop.
while response != "y":
    print("Was the number you were thinking of", str(firstguess) + "?")
    response = input()
    if response == "h":   
        low = firstguess + 1
    elif response == "l":
        high = firstguess - 1
    elif response == "y":
        print ("Got it!")

        # Should never take more than 7 tries.
        if tries > 7:
            print("It took me", tries, "tries to guess it right. I am dissatisfied.")
        elif tries <= 7 and tries > 1:
            print("It took me", tries, "tries to guess it right. I am awesome.")
        elif tries == 1:
            print("It took me", tries, "try. I am a mastermind!")

    # If the user types something incorrect, this will appear.
    else:
        print ("What? I only understand \"h\" for higher, \"l\" for lower, or \"y\" for yes.")
        tries -= 1 # Won't count as a try.

    # Necessary for guesses to be shorter, and for "tries" to be counted.
    firstguess = (low + high)// 2
    tries += 1

input("\nPress the enter key to exit.")
