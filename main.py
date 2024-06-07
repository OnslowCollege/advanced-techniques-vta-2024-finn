while True:
    print("Welcome to Math Test Masterming")
    print(
        "Choose a topic to work on: \n - (G)eneral Subjects Quiz \n - (A)lgebra \n - (P)robability \n - (B)asic Arithmetic \n - (Q)uit",
        "\n - (Q)uit ",
    )

    topic = input("What topic would you like to study: ")
    if topic.upper() == "G":
        general_subjects_quiz()
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
