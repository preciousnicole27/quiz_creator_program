# Main program
# import libraries
import os
import random
from colorama import init, Fore, Style
# initialize color formatting
init(autoreset=True)
# set filename for storing questions along with the existing questions
filename= "quiz_questions.txt"
# define the function that will check files
def check_file():
    if not os.path.exists(filename):
        with open(filename, 'w'): pass
# check if quiz file exists
# define function that will let user add questions
def add_question():
# use loop
    while True:
# ask user to input the correct answer for the given question
        print(Fore.GREEN + "\n Adding the new question")
        question = input("Enter the question:")
        a = input("a.")
        b = input("b.")
        c = input("c.")
        d = input("d.")

        answer = input("Correct answer (a/b/c/d):").strip().lower()
        if answer not in ('a','b','c','d'):
            print(Fore.RED + "Invalid answer")
            continue
# save the question given along with the answer
# ask user if they want to add another question
        with open (filename, 'a') as file:
            file.write(f"Question:{question}\n")
            file.write(f"A. {a}\n")
            file.write(f"B. {b}\n")
            file.write(f"C. {c}\n")
            file.write(f"D. {d}\n")
            file.write(f"Answer: {answer.upper()}\n\n")    
# define the function that will read the questions in the existing text file
def quiz_program(filename):
# store 
# return 
# define the function that will view the questions added 
def view_questions():
# print each question number and text
# define the function that will allow user to remove questions
def remove_question():
# write the updated list after
# define the function that will allow user to take the quiz
def start_quiz(questions, num_questions = 5):
# shuffle/ randomize the questions
# ask for user input (answers)
# print score with percentage
# define the main menu function
def main():
    filename = "quiz_questions.txt"
# loop through four options
# let user choose which they want to do
