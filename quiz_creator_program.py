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
        again = input("Add a new question? (yes/no):").strip().lower()
        if again != 'yes':
            break  
# define the function that will read the questions in the existing text file
def quiz_program(filename):
    check_file()
    with open (filename, 'r') as file:
        lines = file.readlines()

    questions = []
    current = {}
# store 
    for line in lines:
        line = line.strip()
        if line.startswith("Question:"):
            current = {"question":line}
        elif line.startswith("A."):
            current["A"] =  line
        elif line.startswith("B."):
            current["B"] = line
        elif line.startswith("C."):
            current["C"] = line
        elif line.startswith("D."):
            current["D"] = line
        elif line.startswith("Answer:"):
            current["answer"] = line.split(":")[1].strip().upper()
            questions.append(current)
        else:
            continue
# return
    print(f"Loading success {len(questions)} questions.")
    return questions
# define the function that will view the questions added 
def view_questions():
    questions = quiz_program(filename)
    if not questions:
        print(Fore.BLUE + "No questions found.")
        return
# print each question number and text
    for idx, q in enumerate(questions):
        print(Fore.GREEN + f"[{idx}] {q['questions'][9:]}")
# define the function that will allow user to remove questions
def remove_question():
    questions = quiz_program(filename)
    if not questions:
        print(Fore.YELLOW + "No questions to remove")
        return
    view_questions()
# write the updated list after
    try:
        idx = int(input("Enter the number of questions to remove:"))
        if 0 <= idx < len(questions):
            del questions[idx]
            with open(filename, 'w') as file:
                for q in questions[idx]:
                    with open(filename, 'w') as file:
                        file.write(f"{q['question']}\n")
                        file.write(f"{q['A']}\n")
                        file.write(f"{q['B']}\n")
                        file.write(f"{q['C']}\n")
                        file.write(f"{q['D']}\n")
                        file.write(f"Answer: {q['answer']}\n\n")
                print(Fore.GREEN + "Question removed successfully.")
        else:
            print(Fore.RED + "Invalid index.")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")


def main():
    filename = "quiz_questions.txt"
# loop through four options
    while True:
        print(Style.BRIGHT + "\n Welcome to Quiz Creator!")
        print("A. Add question")
        print("B. View questions")
        print("C. Exit")
# let user choose which they want to do
        choice = input("Please choose an option(A/B/C/D):").strip()

        if choice == "A":
            add_question()

        elif choice == "B":
            view_questions()
        
        elif choice == "C":
            print(Fore.PINK + "Thank you!!")
            break
        else:
            print(Fore.RED + "Invalid input. Please try again.")

if __name__ == "__main__":
    main()
