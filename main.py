"""Math Test Mastermind."""
questions: dict[str, dict[str, str]] = {
    "Algebra_1": {"If 2x = 4 what is x?": "2", "If 3x = 9 what is x?": "3",
        "If x + 2 = 10 what is x?": "8", "If 5y + 2 = 12 what is y?": "2",
        "If 2y - 4 = 6 what is y?": "5", "If 3x = 6 what is x?": "2",
        "If y = 16 what is y?": "16", "If 4x = 16 what is x?": "4",
        "If 6z = 18 what is z?": "3", "If 5x = 25 what is x?": "5"},
    "Algebra_2": {"If 2x ÷ 10 = 2 what is x?": "10",
        "If 4y ÷ 2 = 12 what is y?": "6", "If 6x - 4 = 32 what is x?": "6",
        "If 12z - 5 = 19 what is z?": "2", "If 8y x 3 = 24 what is y?": "1",
        "What is x if 2(x + 1) = 18?": "8", "What is z if 8z x 3 = 48?": "2",
        "4(x + 2) = 24 what is x?": "4","If 3x = 20 - 8 what is x?": "4",
        "If 10y = 75 - 5 what is y?": "7",},
    "Algebra_3": {"If c - 20 = 4 - 3c what is c?": "6",
        "If -4(-3n - 8) = 10n + 20 what is n?": "-6",
        "If 5z + 2 = 3z + 14 what is z?": "6",
        "If 4(x - 3) = 2(x + 5) what is x?": "11",
        "If 6y + 12 = 3(2y + 4) what is y?": "0",
        "If 7z - 3 = 4z + 9 what is z?": "4",
        "If 8x + 2 = 3x + 17 what is x?": "3",
        "If 9y - 4 = 5y + 8 what is y?": "3",
        "If 7x - 5 = 2x + 20 what is x?": "5",
        "If 11y + 6 = 3y + 46 what is y?": "5"},
    "Fractions_1": {"What is 1/2 + 1/2?": "1", "What is 1/3 + 1/3?": "2/3",
        "What is 1/4 + 1/2?": "3/4", "What is 3/5 - 1/5?": "2/5",
        "What is 2/3 x 3/4?": "1/2", "What is 3/8 - 1/8": "1/4",
        "What is 2/4 x 1/3?": "1/6", "What is 1/2 + 2/8?": "3/4",
        "What is 4/5 x 1/2?": "2/5", "What is 2/5 x 3/5?": "6/35"},
    "Fractions_2": {"What is 5/12 ÷ 2/3?": "5/8", "What is 4/9 x 3/7?": "4/21",
        "What is 15/4 x 8/3?": "10", "What is 18/25 x 15/24?": "9/20",
        "What is 14/27 ÷ 7/9?": "2/3", "What is 11/15 - 5/8?": "13/120",
        "What is 7/9 x 5/6?": "35/54", "Simplify 24/36": "2/3",
        "Simplify 35/50": "7/10", "Simplify 14/21": "2/3"},
    "Fractions_3": {"What is 2/3(1/5 + 3/4)?": "19/30", 
        "What is 3/4(1/2 + 1/3)?": "5/8", "What is 5/6(2/5 + 1/4?)?": "13/24", 
        "What is 4/5(3/8 + 1/2)?": "7/10", "What is 2/3(1/4 + 3/5)?": "17/30", 
        "What is 5/6(2/5 - 1/4?)?": "1/8", "What is 3/5(1/4 - 2/3)?": "1/10", 
        "What is 4/7(2/3 x 1/6)?": "4/63", "What is 3/4(1/5 + 1/2)?": "21/40", 
        "What is 4/5(1/2 - 1/6)?": "4/15"},
    "Basic_A_1": {"What is 12 ÷ 2?": "6", "What is 22 + 48?": "70",
        "What is 14.5 - 10?": "4.5", "What is 10 x 5?": "50",
        "What is 5.5 + 7.5?": "13", "What is 32 + 16?": "48",
        "What is 13.3 - 6?": "7.3", "What is 14 x 2?": "28",
        "What is 24 ÷ 6?": "4", "What is 18 - 14.2?": "3,8"},
    "Basic_A_2": {"What is (12 x 11) - 10?": "122", 
        "What is (8 x 3) ÷ 4?": "6", "What is 6 ÷ (3 x 2)?": "1", 
        "What is (10 + 5) ÷ 5?": "3", "What is (12 - 4) x 2?": "16", 
        "What is 10 - 8 x 32?": "64", "What is (20 - 5) ÷ 3?": "5", 
        "What is (18 ÷ 3) x 2?": "12", "What is (21 - 7) ÷ 2?": "7", 
        "What is 24 ÷ (4 x 2)?": "3" },
    "Basic_A_3": {"What is 8 x 7 ÷ 14?": "4", "What is 12 x 5 ÷ 15 + 2?": "6", 
        "What is 9 x 4 - 6 ÷ 3?": "34", "What is 10 + 6 x 2 ÷ 4?": "13", 
        "What is 14 x 3 ÷ 7- 1?": "5", "What is 16 - 8 x 2 ÷ 4?": "12", 
        "What is 20 x 9 ÷ (15 + 3)?": "10", "What is (18 - 6) x 5 ÷ 2?": "30", 
        "What is 21 + 6 ÷ 3 x 2?": "25", "What is 9 x (4 - 6) ÷ (3 + 1)?": "-4.5",}
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
