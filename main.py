"""Math Test Mastermind."""
questions: dict[str, dict[str, str]] = {
    "Algebra_1": {"If 2x=4 what is x?": "2", "If 3x=9 what is x?": "x=3", "If x=12 what is x?": "x=12"},
    "Algebra_2": {"If 2x-2=6 what is x?": "4"},
    "Algebra_3": {"4x+3=15": "x=3"},
    "Fractions_1": {"1/2+1/2": "1", "1/3+1/3": "2/3"},
    "Fractions_2": {"2/3x1/3": "2/9"},
    "Fractions_3": {"11/3÷2/3": "5/2"},
    "Basic_A_1": {"3+9": "12"},
    "Basic_A_2": {"4x7": "28"},
    "Basic_A_3": {"8x7+2": "58"},
}


def general_topics_quiz():
    """
    Start All topics quiz.

    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Test general topics quiz")



def algebra(Question_info: dict[str, str], hearts: int) -> int:
    """
    Start Fractions topic.
    
    Parameter
    ---------
    - Gives the questions for the user to answer.
    - Current number of hearts the user has.

    Return
    ------
    - New number of hearts.

    """
    correct_answers = 0
    for question in Question_info:
        answer = Question_info[question]
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

    print(f"You got {correct_answers} out of {len(Question_info)} questions correct!")
    return hearts


def fractions(Question_info: dict[str, str], hearts: int) -> int:
    """
    Start Fractions topic.
    
    Parameter
    ---------
    - Gives the questions for the user to answer.
    - Current number of hearts the user has.

    Return
    ------
    - New number of hearts.

    """
    print("Fractions Quiz")
    correct_answers = 0
    for question in Question_info:
        answer = Question_info[question]
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

    print(f"You got {correct_answers} out of {len(Question_info)} questions correct!")
    return hearts


def basic_arithmetic(Question_info: dict[str, str]):
    """
    Start Basic Arithmetic topic.
    
    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Basic Arithmetic Quiz")
    correct_answers = 0
    for question in Question_info:
        answer = Question_info[question]
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



def select_level(topic):
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