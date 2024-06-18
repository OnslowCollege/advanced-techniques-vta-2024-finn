"""Math Test Mastermind."""
questions: dict[str, dict[str, str]] = {
    "Algebra_1": {"2x=4": "x=2", "3x=9": "x=3", "x=12": "x=12"},
    "Algebra_2": {"2x-2=6": "x=4"},
    "Algebra_3": {"2x-2=6": "x=4"},
    "Fractions_1": {"1+1=2": "2"},
    "Fractions_2": {"1+1=2": "2"},
    "Fractions_3": {"1+1=2": "2"},
    "Basic_A_1": {"3+9": "12"},
    "Basic_A_2": {"3+9": "12"},
    "Basic_A_3": {"3+9": "12"},
    "General_Topics_Quiz": {"3+9": "12"}
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



def fractions(Question_info: dict[str, str]):
    """
    Start Algebra topic.
    
    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Test probability")



def basic_arithmetic(Question_info: dict[str, str]):
    """
    Start Basic Arithmetic topic.
    
    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Test probability")




while True:
    print("Welcome to Math Test Mastermind \n----------------------------- ")
    print(
        "Choose a topic to work on: \n -",
        "(G)eneral Topics Quiz \n - (A)lgebra \n - (P)robability", 
        "\n - (B)asic Arithmetic \n - (Q)uit "
    )

    topic = input("What topic would you like to study: ")
    if topic.upper() == "G":
        general_topics_quiz(questions["General_Topics_Quiz"])
    elif topic.upper() == "A":
        algebra(questions["Algebra_1"])
    elif topic.upper() == "P":
        fractions(questions["Probability_1"])
    elif topic.upper() == "B":
        basic_arithmetic(questions["Basic_A_1"])
    elif topic.upper() == "Q":
        print("Goodbye.")
        break
    else:
        print("Please enter G, A, P, B or Q!")

