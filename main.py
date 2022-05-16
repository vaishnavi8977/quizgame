from game import Game
from context import GameContext


class Context(GameContext):
    """Responsible for handling interaction with the game UI."""

    def __init__(self):
        self.game = Game(self)

    def show_question(self, question):
        """Displays the question to a user."""
        answer = input(question).upper()
        if(answer == "YES"):
            # self.game.answer_yes("You answered YES. Continue?")
            self.game.answerYes.answer_yes(question)
        elif(answer == "NO"):
            self.game.answerNo.answer_no(question)
        else:
            print("Unknown input " + answer)


def main():
    context = Context()
    context.game = Game(context)
    context.game.Start(context).start()
    context.game = None


if __name__ == "__main__":
    main()
