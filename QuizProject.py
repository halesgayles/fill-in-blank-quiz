difficulty_options = ["Easy", "Medium", "Hard"]

easy_question = "The competitive mode that has 3 lanes is called __1__. \n" \
                "The mode that gives random gods/goddesses and only has one lane with no backing is called __2__. \n" \
                "The mode that has two lanes with a large jungle in the middle is called__3__. \n" \
                "The mode that has a colosseum map and counts down tickets is called __4__."
med_question = "The pantheon that includes gods such as Loki, Thor, and Odin is __1__. \n" \
               "The pantheon that includes Athena, Aphrodite, and Zeus is __2__.\n" \
               "The pantheon that includes Chang'e, Hou Yi, and Ne Zha is __3__. \n" \
               "The pantheon that includes Ra, Bastet, and Neith is __4__"
hard_question = "__1__ ultimate ability is called No Escape which chains enemies and pulls them to him with a stun.\n" \
                "__2__ ultimate ability is called Pillar of Agony which pulls enemies in a radius closer to him and does damage.\n" \
                "__3__ ultimate ability is called Sunbreaker which sends the nine suns crashing down dealing damage to enemies.\n" \
                "__4__ ultimate ability is called Hovering Death in which he can take to the skies and execute an enemy if their health is low enough."

easy_answers = ["conquest", "assault", "siege", "arena"]
med_answers = ["Norse", "Greek", "Chinese", "Egyptian"]
hard_answers = ["Ares", "Hades", "Hou Yi", "Thanatos"]

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
def answer_set(question):
    if question == easy_question:
        return easy_answers

    if question == med_question:
        return med_answers

    if question == hard_question:
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
    question = get_difficulty(level)

    answers = answer_set(question)

    blank_index = 0
    answer_index = 0

    while blank_index < len(blanks):
        print question

        user_answer = raw_input("What goes in " + blanks[blank_index] + "?")

        if check_answer(user_answer, answers, answer_index) == "correct":
            print "Correct!"

            question = question.replace(blanks[blank_index], user_answer)

            blank_index += 1
            answer_index += 1

        else:
            while check_answer(user_answer, answers, answer_index) == "incorrect":
                user_answer = raw_input("That wasn't correct! Let's try again.")
            print "Correct!"

            question = question.replace(blanks[blank_index], user_answer)

            blank_index += 1
            answer_index += 1

    print "Congratulations and thanks for taking this quiz!"


quiz()
