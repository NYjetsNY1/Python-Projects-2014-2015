# Ben Sklar
# Trivia with unique point values.
# Uses functions, "global" variables, variables, for and while loops, etc.
# Trivia Challenge 2.0
# Trivia game that reads a plain text file.
# Uses pickling.
# Pickling is the process in which a Python object is converted into a byte stream.
# Unpickling is the inverse operation, in which a byte stream (from a binary file or bytes-like object)
# is converted back into an object.

import sys
import pickle

# First pickle function to pickle three original high scores.
def pickle_three_lists(highscore1, highscore2, highscore3):
    f = open("picklesnew.dat", "wb")
    pickle.dump(highscore1, f)
    pickle.dump(highscore2, f)
    pickle.dump(highscore3, f)
    f.close()


# Second pickle function to pickle-load/read the three original high scores.
def pickle_three_lists_open():
    f = open("picklesnew.dat", "rb")
    highscore1 = pickle.load(f)
    highscore2 = pickle.load(f)
    highscore3 = pickle.load(f)
    f.close()


# Opens the file.
# If file didn't exist, ends program.
def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file


# Reads next line.
def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


# Next block of data.
def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    # Only takes first digit of the multiple-choice-value. So 347 = MC 3.
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file)

    point_value = next_line(the_file)
    if point_value:
        point_value = point_value[0]

    return category, question, answers, correct, explanation, point_value


# Welcomes the player, gets the name, and makes it globally available.
def welcome(title):
    global player1_name
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
    player1_name = input("What is your first name?: ")


# Used to make highscores sortable. 
def getKey(highscores):
    return highscores[1]


# Main funcion.
def main():
    # Made up default highscores.
    highscore1 = ["Benjamin", int(9001)]
    highscore2 = ["Bobby", int(5)]
    highscore3 = ["Rhinosa", int(0)]

    # Pickles the highscores. Even if file doesn't exist, will create.
    pickle_three_lists(highscore1, highscore2, highscore3)
    pickle_three_lists_open()

    # Opens trivia file.
    trivia_file = open_file("trivia1.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # Get first block.
    category, question, answers, correct, explanation, point_value = next_block(trivia_file)

    # You can have an arbitrary amount of questions (while loop not for loop).
    # Each question unique in point value in txt file.
    while category:
        # Ask a question
        print("CATEGORY:", category)
        print("QUESTION:", question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # Get answer
        answer = input("What's your answer?: ")

        # Check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(point_value)
            
        # If wrong 
        else:
            print("\nWrong.", end=" ")

        print(explanation)
        print("Score:", score, "\n\n")

        # Get next block.
        category, question, answers, correct, explanation, point_value = next_block(trivia_file)

    
    # Tells final score, puts it into highscore4.
    print("That was the last question!")
    print("Your final score is", score, ".")
    highscore4 = [player1_name, int(score)]

    # Pickles the new highscore4.
    f = open("picklesnew.dat", "wb")
    pickle.dump(highscore4, f)
    f.close()
    f = open("picklesnew.dat", "rb")
    highscore4 = pickle.load(f)
    f.close()

    # High-score list.
    highscores = [highscore1, highscore2, highscore3, highscore4]
    print("\nHigh Scores List:\n")
    # Prints high-scores by highest number.
    for i in sorted(highscores, key=getKey, reverse=True):
            print("NAME:", [i][0][0], "\t\t\t", "SCORE:", [i][0][1])
 
main()  
input("\n\nPress the enter key to exit.")
