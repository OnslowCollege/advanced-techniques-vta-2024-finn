"""Math Test Mastermind."""
questions: dict[str, dict[str, str]] = {
    "Algebra_1": {"If 2x = 4 what is x?": "2", "If 3x = 9 what is x?": "3",
        "If x = 12 what is x?": "12", "If 5y = 10 what is y?": "2", 
        "If 2y = 10 what is y?": "5", "If 3x = 6 what is x?": "2", 
        "If y = 16 what is y?": "16", "If 4x = 16 what is x?": "4", 
        "If 6z = 18 what is z?": "3", "If 5x = 25 what is x?": "5"},
    "Algebra_2": {"If 2x - 2 = 6 what is x?": "4", 
        "If 4y + 2 = 10 what is y?": "2", "If 4x - 4 = 12 what is x?": "4", 
        "If 12z - 5 = 19 what is z?": "2", "If 8y x 2 = "},
    "Algebra_3": {"If 4x + 3 = 15 what is x?": "3"},
    "Fractions_1": {"1/2 + 1/2": "1", "1/3 + 1/3": "2/3"},
    "Fractions_2": {"2/3 x 1/3": "2/9"},
    "Fractions_3": {"11/3 ÷ 2/3": "5/2"},
    "Basic_A_1": {"3 + 9": "12"},
    "Basic_A_2": {"4 x 7": "28"},
    "Basic_A_3": {"8 x 7 + 2": "58"},
}


def general_topics_quiz(hearts):
    """
    Start All topics quiz.

    Parameter:
    ----------
    -   hearts: Current number of hearts the user has.

    """
    print("Test general topics quiz")
    return hearts


def algebra(question_info: dict[str, str], hearts: int) -> int:
    """
    Start Algebra topic.

    Parameter:
    ---------
    - Question_info: Gives the questions for the user to answer.
    - hearts: Current number of hearts the user has.

    Return:
    ------
    - New heart balance.

    """
    correct_answers = 0
    for question in question_info.keys():
        answer = question_info[question]
        user_answer = input(f"{question}:  ")
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
            if hearts < 5:
                hearts += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
            hearts -= 1
        if hearts <= 0:
            print("You have no more hearts left. Game over!")
            break

    print(f"You got {correct_answers} out of {len(question_info)}",
        "questions correct!")
    return hearts


def fractions(question_info: dict[str, str], hearts: int) -> int:
    """
    Start Fractions topic.

    Parameter:
    ----------
    - questions: Dictionary of questions and answers.
    - hearts: Current number of hearts the user has.

    Return:
    ------
    - New number of hearts.

    """
    print("Fractions Quiz")
    correct_answers = 0

    for question in question_info.keys():
        answer = question_info[question]
        user_answer = input(f"{question}: ")
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
            if hearts < 5:
                hearts += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
            hearts -= 1
        if hearts <= 0:
            print("You have no more hearts left. Game over!")
            break

    print(f"You got {correct_answers} out of {len(question_info)}",
        "questions correct!")
    return hearts


def basic_arithmetic(question_info: dict[str, str], hearts: int) -> int:
    """
    Start Basic Arithmetic topic.

    Parameter:
    ----------
    -   Question_info: Gives the questions for the user to answer.
    -   hearts: Current number of hearts the user has.

    Return:
    ------
    - New number of hearts.

    """
    print("Basic Arithmetic Quiz")
    correct_answers = 0
    for question in question_info.keys():
        answer = question_info[question]
        user_answer = input(f"{question} = ")
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
            if hearts < 5:
                hearts += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
            hearts -= 1
        if hearts <= 0:
            print("You have no more hearts left. Game over!")
            break

    print(f"You got {correct_answers} out of {len(question_info)}",
        "questions correct!")
    return hearts


def select_level(topic):
    """Asks user which level of their topic they will be tested on."""
    while True:
        print("Select a level for {}: ".format(topic))
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        level = input("Enter the level number (1-3): ")
        if level in ["1", "2", "3"]:
            return topic + "_" + level
        else:
            print("Please enter a number between 1 and 3!")

hearts = 5
while True:
    print("Welcome to Math Test Mastermind \n----------------------------")
    print(
        "Choose a topic to work on: \n -",
        "(G)eneral Topics Quiz \n - (A)lgebra \n - (F)ractions",
        "\n - (B)asic Arithmetic \n - (Q)uit "
    )

    topic = input("What topic would you like to study: ").upper()
    if topic == "G":
        hearts = general_topics_quiz(hearts)
    elif topic == "A":
        selected_level = select_level("Algebra")
        hearts = algebra(questions[selected_level], hearts)
    elif topic == "F":
        selected_level = select_level("Fractions")
        hearts = fractions(questions[selected_level], hearts)
    elif topic == "B":
        selected_level = select_level("Basic_A")
        hearts = basic_arithmetic(questions[selected_level], hearts)
    elif topic == "Q":
        print("Goodbye.")
        break
    else:
        print("Please enter G, A, F, B or Q!")
    print(f"You have {hearts} hearts left.")
    if hearts <= 0:
        print("You have no more hearts left. You lose!")
        break
