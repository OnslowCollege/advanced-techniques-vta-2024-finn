"""Math Test Mastermind."""
questions: dict[str, dict[str, str]] = {
    "Algebra_1": {" if 2x=4 what is x?": "x=2", "3x=9": "x=3", "x=12": "x=12"},
    "Algebra_2": {"2x-2=6": "x=4"},
    "Algebra_3": {"4x+3=15": "x=3"},
    "Fractions_1": {"1/2+1/2": "1", "1/3+1/3": "2/3"},
    "Fractions_2": {"2/3x1/3": "2/9"},
    "Fractions_3": {"11/3÷2/3": "5/2"},
    "Basic_A_1": {"3+9": "12"},
    "Basic_A_2": {"4x7": "28"},
    "Basic_A_3": {"8x7+2": "58"},
}


def general_topics_quiz(Question_info: dict[str, str]):
    """
    Start All topics quiz.

    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Test algebra")


def algebra(Question_info: dict[str, str]):
    """
    Start Algebra topic.
    
    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.
    
    """
    print("Test algebra")
    correct_answers = 0
    for question in Question_info:
        answer = Question_info[question]
        user_answer = input(f"{question} = ")
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")

    print(f"You got {correct_answers} out of {len(Question_info)} questions correct.")





def fractions(Question_info: dict[str, str]):
    """
    Start Algebra topic.
    
    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Fractions Quiz")
    correct_answers = 0
    for question in Question_info:
        answer = Question_info[question]
        user_answer = input(f"{question} = ")
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")

    print(f"You got {correct_answers} out of {len(Question_info)} questions correct.")



def basic_arithmetic(Question_info: dict[str, str]):
    """
    Start Basic Arithmetic topic.
    
    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Test probability")


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


while True:
    print("Welcome to Math Test Mastermind \n----------------------------")
    print(
        "Choose a topic to work on: \n -",
        "(G)eneral Topics Quiz \n - (A)lgebra \n - (F)ractions", 
        "\n - (B)asic Arithmetic \n - (Q)uit "
    )

    topic = input("What topic would you like to study: ").upper()
    if topic.lower() == "g":
        selected_level = select_level("General Topics")
        general_topics_quiz(selected_level) 
    elif topic.lower() == "a":
        selected_level = select_level("Algebra")
        algebra(questions[selected_level])
    elif topic.lower() == "f":
        selected_level = select_level("Fractions")
        fractions(questions[selected_level])  
    elif topic.lower() == "b":
        selected_level = select_level("Basic Arithmetic")
        basic_arithmetic(questions[selected_level])
    elif topic.lower() == "q":
        print("Goodbye.")
        break
    else:
        print("Please enter G, A, F, B or Q!")

