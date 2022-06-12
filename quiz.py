from collections import OrderedDict

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Incorrect")
        return 0


def display_score(correct_guesses, guesses):
    print("------------------------")
    print("RESULTS")
    print("------------------------")
    print("Answers: ")
    for i in questions:
        print(questions.get(i))
    print()
    print("Guesses: ")
    for i in guesses:
        print(i)
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your Score is: "+str(score)+"%")
#------------------------------------
def play_agian():
    pass

questions = OrderedDict({
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "What is Earth's gravitational pull?: ": "C",
    "Is the Earth a sphere?:": "D"
})

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. 1.6", "B. 24.7", "C. 9.8", "D. 3.7"],
          ["A. What's Earth?", "B. False", "C. Sometime", "D. True"]]

print(new_game())
