from calendar import c
from context import GameContext


class Game:
    """ Yes/No question game. It presents a sequence of questions to a user. The sequence changes
    depending on the user's answers to the previous questions.
    """

    def __init__(self, context: GameContext):
        # Use self.context to interact with the UI. For example, to display a question or exit the game.
        self.context = context
        self.answerYes = self.AnswerYes(context)
        self.answerNo = self.AnswerNo(context)

    class Start:
        def __init__(self, context: GameContext):
            self.context = context

        def start(self):
            """It's called when a user is ready to play the game.
        Handles the game setup, such as showing the initial question.
        """
        # self.context.show_question("Welcome to the game! "
        #                            "Think of a design pattern and answer these following yes/no questions. "
        #                            "Ready?")
            self.context.show_question(self.context.questions[0]["question"])


    class AnswerYes:
        def __init__(self, context: GameContext):
            self.context = context

        def answer_yes(self, question):
            """It's called when a user answers YES to a question.
         Handles the transition to the next question or exits the game.
         """

            for x in self.context.questions:
                if x["question"] == question:
                    next_question_id = int(x["yes"])
                    if next_question_id == 0:
                        self.context.end_game()
                    else:
                        for x in self.context.questions:
                            if x["id"] == next_question_id:
                                next_question = x["question"]
                                self.context.show_question(next_question)
