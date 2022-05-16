class GameContext:
    """Responsible for handling interaction with the game UI."""

    questions = [
        {
            "id": 1,
            "question": "Welcome to the game! Think of a design pattern and answer these following yes/no questions. Ready?",
            "yes": 2,
            "no": 0
        },
        {
            "id": 2,
            "question": "Does it provide the object creation mechanism that enhance the flexibilities of the existing code?",
            "yes": 5,
            "no": 3
        },
        {
            "id": 3,
            "question": "Is it responsible for how one class communicates with others?",
            "yes": 6,
            "no": 4
        },
        {
            "id": 4,
            "question": "Does it explain how to assemble objects and classes into a larger structure and simplifies the structure by identifying the structure by identifying the relationships?",
            "yes": 7,
            "no": 19
        },
        {
            "id": 5,
            "question": "Does it ensure you have at most one instance of a class in your application?",
            "yes": 10,
            "no": 11
        },
        {
            "id": 6,
            "question": "Does it provide a mechanism to the context to change its behavior?",
            "yes": 8,
            "no": 9
        },
        {
            "id": 7,
            "question": "Does it attach additional behavior to an object dynamically at run-time?",
            "yes": 16,
            "no": 17
        },
        {
            "id": 8,
            "question": "Is changing behavior built into the scheme?",
            "yes": 12,
            "no": 13
        },
        {
            "id": 9,
            "question": "Does it allow a group of objects to be notified when some state changes?",
            "yes": 14,
            "no": 15
        },
        {
            "id": 10,
            "question": "Is it Singleton Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 11,
            "question": "Is it Builder Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 12,
            "question": "Is it State Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 13,
            "question": "Is it Strategy Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 14,
            "question": "Is it Observer Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 15,
            "question": "Is it Command Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 16,
            "question": "Is it Decorator Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 17,
            "question": "Is it Adapter Pattern?",
            "yes": 18,
            "no": 19
        },
        {
            "id": 18,
            "question": "Woohoo! I guessed it! Try again?",
            "yes": 1,
            "no": 0
        },
        {
            "id": 19,
            "question": "Oops! Something went wrong! Try again?",
            "yes": 1,
            "no": 0
        },

    ]

    def show_question(question):
        """Displays the question to a user.


        question - line ot be shown
        """
        pass

    def end_game():
        """Exits the game."""
        pass
