import os

def register_user():
    """
    Registers a new user by storing their credentials in a file.
    """
    print("             Register as a user           ")
    name = input("Enter your name: ").lower()
    password = input("Enter your password: ").lower()
    try:
        with open("users.txt", "a") as file:
            file.write(f"{name},{password}\n")
        print("Registration successful!\n")
    except Exception as e:
        print(f"An error occurred while registering: {e}")


def login_user():
    """
    Authenticates the user using stored credentials.
    """
    print("              Login          ")
    while True:
        username = input("Enter your user name: ").lower()
        password = input("Enter your password: ").lower()
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    stored_username, stored_password = user.strip().split(",")
                    if username == stored_username and password == stored_password:
                        print("Login successful!\n")
                        return True
                print("Invalid credentials. Please try again.\n")
        except FileNotFoundError:
            print("No registered users found. Please register first.\n")
            return False
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return False


def quiz():
    """
    Conducts the quiz, calculates the score, and writes results to a file.
    """
    questions = (
        "Which data structure can be used to implement function call recursion?",
        "In a directed acyclic graph (DAG), which of the following algorithms is used to find the topological ordering of the vertices?",
        "Which type of tree traversal visits the nodes in the order: root, left subtree, right subtree?",
        "Which collision resolution technique in hashing uses a linked list to store multiple values at the same hash index?",
        "Which of the following algorithms is used for finding the shortest path in an unweighted graph?"
    )

    options = (
        ("A) Queue ", "B) Stack ", "C) Array ", "D) Heap"),
        ("A) Kruskal's Algorithm", "B) Dijkstra's Algorithm", "C) Topological Sort ", "D) Floyd-Warshall Algorithm"),
        ("A) In-order ", "B) Post-order ", "C) Pre-order", "D) Level-order"),
        ("A) Linear probing ", "B) Quadratic probing", "C) Separate chaining ", "D) Double hashing"),
        ("A) Dijkstra's Algorithm", "B) Depth-First Search (DFS)", "C) Breadth-First Search (BFS)", "D) Prim's Algorithm")
    )

    answers = ("B", "C", "C", "C", "C")
    guesses = []
    score = 0
    question_num = 0

    print("----------Quiz--------\n")
    try:
        for question in questions:
            print("------------------------------------------------------")
            print(question)
            for option in options[question_num]:
                print(option)

            guess = input("Enter (A, B, C, D): ").upper()
            guesses.append(guess)
            if guess == answers[question_num]:
                score += 1
                print("CORRECT")
            else:
                print("INCORRECT")
                print(f"{answers[question_num]} is the CORRECT answer.")
            question_num += 1

        print("--------------------------")
        print("            RESULT        ")
        print("--------------------------")

        print("Answers: ", end="")
        for answer in answers:
            print(answer, end=" ")
        print()

        print("Guesses: ", end="")
        for guess in guesses:
            print(guess, end=" ")
        print()

        score_percentage = (score / len(questions)) * 100
        print(f"Your score is: {score_percentage}%")

        # Save results to a file
        with open("results.txt", "a") as result_file:
            result_file.write(f"Score: {score_percentage}%\n")

        print("\nResults saved successfully.")
    except Exception as e:
        print(f"An error occurred during the quiz: {e}")


# Main Program
while True:
    print("----------------Online Test------------------\n\n")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        if login_user():
            quiz()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
