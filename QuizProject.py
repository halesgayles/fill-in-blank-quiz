# questions for each level of difficulty
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

# dictionary for questions per difficulty
difficulty = {
    "Easy": easy_question,
    "Medium": med_question,
    "Hard": hard_question
}

# answer set for each difficulty of question
easy_answers = ["conquest", "assault", "siege", "arena"]
med_answers = ["Norse", "Greek", "Chinese", "Egyptian"]
hard_answers = ["Ares", "Hades", "Hou Yi", "Thanatos"]

# dictionary for answer sets per difficulty
answer = {
    "Easy": easy_answers,
    "Medium": med_answers,
    "Hard": hard_answers
}

blanks = ["__1__", "__2__", "__3__", "__4__"]


def check_answer(user_answer, answers, blank_index):
    """
    checks to see if the users answer is correct
    :param user_answer: users answer from input
    :param answers: answer set to check against
    :param blank_index: index of the answer set
    :return:
    """
    if user_answer == answers[blank_index]:
        return "correct"
    else:
        return "incorrect"


# this puts it all together and executes the quiz
def quiz():
    level = raw_input("Choose your level. Easy, Medium or Hard?")

    # as long as the user doesnt enter something in the difficulty dictionary, they're prompted again
    while level not in difficulty:
        level = raw_input("Incorrect difficulty. Try again.")

    question = difficulty[level]
    answers = answer[level]

    blank_index = 0

    # while the blank index is less than the list for blanks then iterate through
    while blank_index < len(blanks):
        print question

        # get user input for answer and set it equal to user_answer
        user_answer = raw_input("What goes in " + blanks[blank_index] + "?")

        # while user answer isn't correct, prompt user again for answer again
        while check_answer(user_answer, answers, blank_index) == "incorrect":
            user_answer = raw_input("That wasn't correct! Let's try again.")
        print "Correct!"

        # replaces the answer in the question
        question = question.replace(blanks[blank_index], user_answer)

        blank_index += 1

    print question
    print "Congratulations and thanks for taking this quiz!"


quiz()