"""Math Test Mastermind."""
questions: dict[str, dict[str, str]] = {
    "Algebra_1": {"2x=4": "x=2", "3x=9": "x=3", "x=12": "x=12"}
    "Algebra_2": {"2x-2="}

}


def general_topics_quiz():
    """Quiz for all topics and levels of those topics."""
    print("Test general topics quiz")

def algebra(Question_info: dict[str, str]):
    """
    Start Algebra topic.
    
    Parameters
    ----------
    -   Question_info: Gives the questions for the user to answer.

    """
    print("Test algebra")


def probability():
    """Start Probability topic."""
    print("Test probability")

def basic_arithmetic():
    """Start Basic Arithmetic topic."""
    print("Test basic arithmetic")




while True:
    print("Welcome to Math Test Mastermind \n----------------------------- ")
    print(
        "Choose a topic to work on: \n -",
        "(G)eneral Topics Quiz \n - (A)lgebra \n - (P)robability", 
        "\n - (B)asic Arithmetic \n - (Q)uit "
    )

    topic = input("What topic would you like to study: ")
    if topic.upper() == "G":
        general_topics_quiz()
    elif topic.upper() == "A":
        algebra(questions["Algebra_1"])
    elif topic.upper() == "P":
        probability()
    elif topic.upper() == "B":
        basic_arithmetic()
    elif topic.upper() == "Q":
        print("Goodbye.")
        break
    else:
        print("Please enter G, A, P, B or Q!")