# Quiz Game Program
# import libraries
import os
import random
from colorama import init, Fore, Style
# init color format auto reset every print
init(autoreset=True)
# define file for quiz questions
filename = "quiz_questions.txt"
# define the function that will check if the quiz file exists
def check_file():
    if not os.path.exists(filename):
        print(Fore.RED + "Quiz file not found.")
        return False
    return True
# if not found return false
# define the function that will load the questions
def load_questions():
    if not check_file():
    # if file doesnt exist return an empty list
        return []
# return
    with open(filename, 'r') as file:
            lines = file.readlines()

    questions = []
    current = {}
    for line in lines:
            line = line.strip()
            if line.startswith("Question:"):
                current = {"question": line[9:].strip()}
            elif line.startswith("A."):
                current["A"] = line[2:].strip()
            elif line.startswith("B."):
                current["B"] = line[2:].strip()
            elif line.startswith("C."):
                current["C"] = line[2:].strip()
            elif line.startswith("D."):
                current["D"] = line[2:].strip()
            elif line.startswith("Answer:"):
                current["answer"] = line.split(":")[1].strip().upper()
                questions.append(current)
    return questions
# define the funnction that will randomize questions
def quiz_user(questions):
    if not questions:
        print(Fore.YELLOW + "No questions available to quiz.")
        return

    score = 0
    total_questions = min(5, len(questions))
# display score
# define the function of the main menu
# use loop to show main menu 
# print menu options
# call main function to begin the program