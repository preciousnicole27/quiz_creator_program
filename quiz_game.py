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
# define the funnction that will randomize questions
# display score
# define the function of the main menu
# use loop to show main menu 
# print menu options
# call main function to begin the program