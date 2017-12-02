difficulty_options = ["Easy", "Medium", "Hard"]

easy_question = "this is __1__ __2__ __3__ __4__"
med_question = "this is medium"
hard_question = "this is hard"

easy_answers = ["e", "a", "s", "y"]
med_answers = ["med answer"]
hard_answers = ["hard answer"]

blanks = ["__1__", "__2__", "__3__", "__4__"]


def get_difficulty(level):
    while level not in difficulty_options:
        level = raw_input("Sorry! You didn't correctly enter a difficulty. Try again!")

    if level == difficulty_options[0]:
        return easy_question

    if level == difficulty_options[1]:
        return med_question

    if level == difficulty_options[2]:
        return hard_question


# gets level appropriate answer set
def answer_set(difficulty):
    if difficulty == easy_question:
        return easy_answers

    if difficulty == med_question:
        return med_answers

    if difficulty == hard_question:
        return hard_answers


# checks if users answer is correct
def check_answer(user_answer, answers, answer_index):
    if user_answer == answers[answer_index]:
        return "correct"
    else:
        return "incorrect"


# this puts it all together and executes the quiz
def quiz():
    # prompts user for level of difficulty
    level = raw_input("Choose your level. Easy, Medium or Hard?")
    difficulty = get_difficulty(level)

    answers = answer_set(difficulty)

    blank_index = 0
    answer_index = 0

    while blank_index < len(blanks):
        print difficulty

        user_answer = raw_input("What goes in " + blanks[blank_index] + "?")

        if check_answer(user_answer, answers, answer_index) == "correct":
            print "Correct!"

            difficulty = difficulty.replace(blanks[blank_index], user_answer)

            blank_index += 1
            answer_index += 1

        else:
            while check_answer(user_answer, answers, answer_index) == "incorrect":
                user_answer = raw_input("That wasn't correct! Let's try again.")

    print "Congratulations and thanks for taking this quiz!"


quiz()