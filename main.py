"""Math Test Mastermind."""

def general_topics_quiz():
    """Quiz for all topics and levels of those topics."""
    print("Test general topics quiz")

def algebra():
    """Start Algebra topic."""
    print("Test algebra")
def probability():
    """Start Probability topic."""
    print("Test probability")

def basic_arithmetic():
    """Start Basic Arithmetic topic."""
    print("Test basic arithmetic")




while True:
    print("Welcome to Math Test Masterming")
    print(
        "Choose a topic to work on: \n - (G)eneral Topics Quiz \n - (A)lgebra \n - (P)robability \n - (B)asic Arithmetic \n - (Q)uit",
        "\n - (Q)uit ",
    )

    topic = input("What topic would you like to study: ")
    if topic.upper() == "G":
        general_topics_quiz()
    elif topic.upper() == "A":
        algebra()
    elif topic.upper() == "P":
        probability()
    elif topic.upper() == "B":
        basic_arithmetic()
    elif topic.upper() == "Q":
        print("Goodbye.")
        break
    else:
        print("Please enter G, A, P, B or Q!")
